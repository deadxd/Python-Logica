# Exercicio resolvido por Cesar Augusto Numero 70 24/01/23
# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar. No final mostre:
# A)Qual é o total gasto na compra.
# B)Quantos produtos custam mais de R$1000.
# C)Qual é o nome do produto mais barato.

continuar = 'S'
count_produtos = 0
soma_produtos = 0
produto_barato_preco = 0
produto_barato_nome = 0
count = 0

while True:
    if continuar == 'S':
        nome = str(input('Informe nome do produto: ')).strip().upper()
        preco = float(input('Informe preço do produto: '))
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        count += 1
        soma_produtos += preco

        if preco > 1000:
            count_produtos += 1

        if count == 1:
            produto_barato_preco = preco
            produto_barato_nome = nome

        if produto_barato_preco > preco:
            produto_barato_preco = preco
            produto_barato_nome = nome
    else:
        break
print(
    f'O preço total das compras é: {soma_produtos} \nNúmero de produtos que custam acima de R$1000 é: {count_produtos} \nProduo mais barato é: {produto_barato_nome}')
