# Exercicio resolvido por Cesar Augusto Numero 25 19/01/23
# crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome.

nome_completo = str(
    input('Insira seu nome completo para tratamento: ')).strip()

print(
    f'O nome: {nome_completo} tem Silva no nome? {"SILVA" in nome_completo.upper()}')
