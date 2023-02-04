# Exercicio resolvido por Cesar Augusto Numero 94 27/01/23
# Crie um programa que leia nome, sexo e idade de vários pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionarios em uma lista
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) A média de idade do grupo.
# C) Uma lista com todas as mulheres.
# D) Uma lista com todas as pessoas com idade acima da média

pessoa = {}
pessoas = []
count = 0
soma_idade = 0

while True:
    pessoa['nome'] = str(input('Informe seu nome: ')).strip().upper()
    # Valindando Caracteres com while até resposta certa
    while True:
        pessoa['sexo'] = str(
            input('Informe seu sexo [M][F]:  ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print(f'Erro digite apenas M ou F')
    # Valindando Caracteres com while até resposta certa
    while True:
        idade = input("Informe sua idade: ")
        if idade.isnumeric():
            idade = int(idade)
            pessoa['idade'] = idade
            break
        print("Entrada inválida, por favor insira somente números inteiros.")

    pessoas.append(pessoa.copy())
    soma_idade += idade
    count += 1

    # Valindando Caracteres com while até resposta certa
    while True:
        perguntar = str(input('Deseja continuar? [S][N] ')).upper().strip()[0]
        if perguntar in 'SN':
            break
        print(f'Erro digite apenas S OU N')
    if perguntar == 'N':
        break

media = soma_idade / count

print(f'Pessoas cadastradas: {count}')
print(f'Media de idade do grupo: {media:5.2f}')

print(f'Nome de mulheres na lista: ')
for c in range(0, len(pessoas)):
    if pessoas[c]['sexo'] == 'F':
        print(f'{pessoas[c]["nome"]}', end=', ')
print()
print(f'Pessoas acima da idade media: ')
for c in range(0, len(pessoas)):
    if pessoas[c]['idade'] > media:
        print(f'{pessoas[c]["nome"]}', end=', ')
