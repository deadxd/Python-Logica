# Exercicio resolvido por Cesar Augusto Numero 37 20/01/23
# Escreva um programa que leia um número inteiro e o usuario decida se quer converter em Binario, Octal ou Hexadecimal

numero = int(input('Informe um número: '))
opcao = int(
    input('ESCOLHA 1: Binario \nESCOLHA 2: Octal \nESCOLHA 3: Hexadecimal: \n'))

if opcao == 1:
    print(f'O valor {numero} em Binario é: {bin(numero) [2:]}')
elif opcao == 2:
    print(f'O valor {numero} em Octal é: {oct(numero) [2:]}')
else:
    print(f'O valor {numero} em Hexadecimal é: {hex(numero) [2:]}')
