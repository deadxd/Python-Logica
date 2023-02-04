# Exercicio resolvido por Cesar Augusto Numero 82 25/01/23
# Crie um programa que vai ler vários números e colocar em uma lista
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares
# No final mostre: o conteúdo das 3 listas geradas

numeros = []
numeros_par = []
numeros_impar = []
resposta = 'S'

while resposta == 'S':
    validado = int(input('Infome um número inteiro: '))
    numeros.append(validado)
    resposta = str(input('deseja continuar? [S][N]: ')).strip().upper()

    if validado % 2 == 0:
        numeros_par.append(validado)
    elif validado % 2 == 1:
        numeros_impar.append(validado)

print(
    f'A primeira lista é: {numeros} \nA lista par é {numeros_par} \nA lista Impar é: {numeros_impar}')
