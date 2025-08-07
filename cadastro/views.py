from django.shortcuts import render, redirect
from .models import Produto, Cliente, Comanda, Caixa

def cadastros_home(request):
    return render(request, 'cadastros_home.html')

def cadastro_produto(request):
    erro = None
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        ativo = request.POST.get('ativo') == 'on'  # checkbox

        # Validação simples
        if not nome or not preco:
            erro = 'Nome e preço são obrigatórios.'
        else:
            try:
                preco = float(preco)
                produto = Produto(nome=nome, descricao=descricao, preco=preco, ativo=ativo)
                produto.save()
                return redirect('index')
            except ValueError:
                erro = 'Preço inválido.'

    return render(request, 'cadastro_produto.html', {'erro': erro})

def cadastro_cliente(request):
    erro = None
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf_cnpj = request.POST.get('cpf_cnpj')
        telefone = request.POST.get('telefone')
        info = request.POST.get('info')

        if not nome or not cpf_cnpj:
            erro = 'Nome e CPF/CNPJ são obrigatórios.'
        else:
            cliente = Cliente(nome=nome, cpf_cnpj=cpf_cnpj, telefone=telefone, info=info)
            cliente.save()
            return redirect('index')

    return render(request, 'cadastro_cliente.html', {'erro': erro})

def cadastro_caixa(request):
    erro = None
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        valor = request.POST.get('valor')
        descricao = request.POST.get('descricao')

        if tipo not in ['entrada', 'saida']:
            erro = 'Tipo inválido.'
        try:
            valor = float(valor)
        except (ValueError, TypeError):
            erro = 'Valor inválido.'

        if not erro:
            caixa = Caixa(tipo=tipo, valor=valor, descricao=descricao)
            caixa.save()
            return redirect('index')

    return render(request, 'cadastro_caixa.html', {'erro': erro})