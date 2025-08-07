from django.contrib import admin
from .models import Produto, Cliente, Comanda, ItemComanda, Caixa

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'ativo')
    list_filter = ('ativo',)
    search_fields = ('nome', 'descricao')
    list_editable = ('preco', 'ativo')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf_cnpj', 'telefone')
    search_fields = ('nome', 'cpf_cnpj', 'telefone')

class ItemComandaInline(admin.TabularInline):
    model = ItemComanda
    extra = 1  # Quantidade de linhas extras para adicionar itens
    autocomplete_fields = ['produto']

@admin.register(Comanda)
class ComandaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'data', 'valor_total')
    list_filter = ('data',)
    search_fields = ('cliente__nome',)
    inlines = [ItemComandaInline]

    def valor_total(self, obj):
        return f'R$ {obj.total():.2f}'
    valor_total.short_description = 'Total'

@admin.register(Caixa)
class CaixaAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'valor', 'data', 'descricao')
    list_filter = ('tipo', 'data')
    search_fields = ('descricao',)
