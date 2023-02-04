# Exercicio resolvido por Cesar Augusto Numero 38 20/01/23
# Escreva um programa que leia 2 números inteiro e compare-os, mostrando na tela uma mensagem:
# -SE O primeiro valor é maior,
# -SE O segundo valor é maior,
# -SE Não existe valor maior, os dois são iguais

primero_numero = int(input('Informe o Primeiro Número: '))
segundo_numero = int(input('Informe o Segundo Número: '))

if primero_numero > segundo_numero:
    print(f'{primero_numero} é maior que {segundo_numero} ')
elif segundo_numero > primero_numero:
    print(f'{primero_numero} é menor que {segundo_numero} ')
else:
    print(f'{primero_numero} é igual a: {segundo_numero}')
