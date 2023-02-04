# Exercicio resolvido por Cesar Augusto Numero 12 16/01/23
# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

preco = float(input('Informe o preço do produto para o desconto: '))
preco_desconto = preco - (preco/100)*5
print(
    f'O produto X com preço R${preco}Reais, agora está com desconto de 5% por R${preco_desconto :0.2f}Reais')
