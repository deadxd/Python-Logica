# Exercicio resolvido por Cesar Augusto Numero 52 21/01/23
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Informe um número inteiro: '))

# Metodo 1

if numero % 2 == 0 and numero != 2 or numero % 3 == 0 and numero != 3 or numero == 1:
    print(f'O número {numero} não é primo')

else:
    print(f'O número {numero} é primo')


# Metodo 2
count = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        print(f'\033[34m')
        count += 1
    else:
        print(f'\033[33m')
    print(i)

if count <= 2 and numero != 1:
    print(f'O número {numero} É primo')
else:
    print(f'O número {numero} não é primo')
