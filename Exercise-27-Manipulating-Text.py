# Exercicio resolvido por Cesar Augusto Numero 26 19/01/23
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
# ex: Cesar Augusto Lima Teixeira Primeiro = Cesar Último = Teixeira

nome_completo = str(
    input('Informe seu nome completo para tratamento: ')).strip()
nome_completo_lista = nome_completo.split()
nome_completo_index = len(nome_completo_lista)

print(nome_completo_lista[0])
print(nome_completo_lista[nome_completo_index-1])
