# Exercicio resolvido por Cesar Augusto Numero 69 24/01/23
# Crie um programa que leia a idade e sexo de varias pessoas. cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

continuar = 'S'
count_18 = 0
count_homens = 0
count_mulheres_20 = 0

while True:
    if continuar == 'S':
        idade = int(input('Informe sua idade: '))
        sexo = str(input('Inform seu Sexo: [M/F] ')).strip().upper()[0]
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

        if idade >= 18:
            count_18 += 1
        if sexo == 'M':
            count_homens += 1
        if idade < 20 and sexo == 'F':
            count_mulheres_20 += 1

    else:
        break
print(
    f'Pessoas com mais de 18 anos: {count_18} \nHomens cadastrados: {count_homens} \nMulheres cadastradas {count_mulheres_20}')
