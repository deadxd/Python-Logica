# Exercicio resolvido por Cesar Augusto Numero 54 21/01/23
# crie um programa que leia o ano de nascimento de sete pessoas. no final, mostre quantas pessoas ainda não atigiram a maioridade e quantas já são maiores. maioridade = 21 anos

from datetime import date
qnt_pessoas_maior = 0
qnt_pessoas_menor = 0

for i in range(1, 8):
    ano_nascimento = int(input(f'Informe a {i} vez o ano de nascimento:'))
    idade = date.today().year - ano_nascimento

    if idade >= 21:
        qnt_pessoas_maior += 1
    else:
        qnt_pessoas_menor += 1

print(
    f'Quantidade de pessoas que já atingiram a maior idade é: {qnt_pessoas_maior} \nQuantidade de pessoas que aida não atingiram a maior idade é: {qnt_pessoas_menor}')
