from django.db import models

# Produtos
class Produto(models.Model):
    nome = models.CharField(max_length=80)
    descricao = models.TextField(max_length=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

# Clientes
class Cliente(models.Model):
    nome = models.CharField(max_length=80)
    cpf_cnpj = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15)
    info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
    
# Comandas
class Comanda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True)
    desconto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    gorjeta = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def total(self):
        subtotal = sum(item.produto.preco * item.quantidade for item in self.itens.all() if item.produto)
        return subtotal - self.desconto + self.gorjeta

    def __str__(self):
        return f'Comanda {self.id} - Total: R$ {self.total():.2f}'

    
# Itens da Comanda
class ItemComanda(models.Model):
    comanda = models.ForeignKey(Comanda, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, null=True)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        produto_nome = self.produto.nome if self.produto else "Produto removido"
        return f'{self.quantidade} x {produto_nome} - Comanda {self.comanda.id}'
    
# Saídas e Entradas do Caixa
class Caixa(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=10, choices=[('entrada', 'Entrada'), ('saida', 'Saída')])
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=True, null=True) #Descrição automática quando vem entrada da comanda (Ex.: 'Venda da Comanda 1')

    def __str__(self):
        return f'{self.tipo.capitalize()} - R$ {self.valor} em {self.data.strftime("%d/%m/%Y %H:%M")}'