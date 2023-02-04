# Exercicio resolvido por Cesar Augusto Numero 10 16/01/23
# Crie um programa que leia quanto dinheiro uma pessoa tem e mostre quantos dolares ela pode comprar
# Dolar a U$1,00 = R$5,14

dinheiro = float(input('Quanto dinheiro você tem? R$'))
dolar = float(5.14)

print(
    f'Com R${dinheiro}Reais você pode comprar U${(dinheiro/dolar) :0.2f}Dolares')
