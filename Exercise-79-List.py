# Exercicio resolvido por Cesar Augusto Numero 79 25/01/23
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista
# caso o número já exista lá dentro, ele não será adicionado.
# No final, mostre todos os valores únicos digitados, em ordem crescente
numeros = []
resposta = 'S'

while resposta == 'S':
    validado = int(input('Infome um número inteiro: '))
    if numeros.count(validado) == 0:
        numeros.append(validado)
        resposta = str(
            input('número cadastrado! deseja continuar? [S][N]: ')).strip().upper()
    else:
        resposta = str(
            input('O número já existe deseja continuar? [S][N]: ')).strip().upper()

numeros.sort()
print(f'Os valores digitados foram: {numeros}')
