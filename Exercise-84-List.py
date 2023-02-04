# Exercicio resolvido por Cesar Augusto Numero 84 26/01/23
# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = []
pessoas_leves = []
pessoas_pesadas = []
count = 0
maior_peso = 0
menor_peso = 0

while True:
    # Cadastrando pessoas e numero de cadastro
    validacao_nome = str(input('Informe o nome da pessoa: ')).strip()
    pessoas.append(validacao_nome)
    validacao_peso = float(input('Informe o peso da pessoa: '))
    pessoas.append(validacao_peso)
    resposta = str(input('Quer continuar? [S][N]: ')).strip().lower()
    if resposta in 'Nn':
        break
    if count == 0:
        maior_peso = validacao_peso
        menor_peso = validacao_peso
    count += 1
    # Validando o mais pesado
    if validacao_peso >= 100:
        pessoas_pesadas.append(validacao_nome)
        pessoas_pesadas.append(validacao_peso)
        if validacao_peso > maior_peso:
            maior_peso = validacao_peso
    # Validando o mais leve
    elif validacao_peso <= 70:
        pessoas_leves.append(validacao_nome)
        pessoas_leves.append(validacao_peso)
        if validacao_peso < menor_peso:
            menor_peso = validacao_peso

print(
    f'Pessoas cadastradas: {count} \nO maior peso foi: {maior_peso}Kg \nO menor peso foi: {menor_peso}Kg')

print(f'A lista de pessoas leve é: ', end=' ')
for p in range(0, len(pessoas_leves), 2):
    print(pessoas_leves[p], end=' ')

print(f'\nA lista de pessoas pesadas é: ', end=' ')
for j in range(0, len(pessoas_pesadas), 2):
    print(pessoas_pesadas[j], end=' ')
