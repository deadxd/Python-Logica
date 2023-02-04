# Exercicio resolvido por Cesar Augusto Numero 57 23/01/23
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = 'A'

while sexo not in 'MF':

    sexo = str(input(
        'Insira um valor correto sendo F para feminino ou M para Masculino: ')).strip().upper()[0]

print(f'O sexo informado foi: {sexo}, até logo ! ')
