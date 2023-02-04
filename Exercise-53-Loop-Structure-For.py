# Exercicio resolvido por Cesar Augusto Numero 53 21/01/23
# crie um programa que leia uma frase qualquer e diga se ela é um palindromo. desconsiderando os espaços.
# Ex: APOS A SOPA   A SACADA DA CASA


frase = str(input('Insira uma frase pra saber se é Palindromo: ')
            ).strip().lower()

# Alem do replace, pode transformar em Lista usando split() e somar a lista sem espaco ''.join()
frase_format = frase.replace(' ', '')

frase_lenght = len(frase_format)

# Metodo 1 usando slice

if frase_format == frase_format[::-1] and frase_format != '':
    print(f'A Frase: {frase} é Palidromo')
else:
    print(f'A Frase: {frase} não é Palindromo')

# Metodo 2 função recursiva:


def formatar_string(string):
    if len(string) == 0:
        return ''
    else:
        print(f'{string[-1]}  {string[:-1]} == {string}')
        # Vai retornar a última letra e somar com o final sem a última letra assim, invertendo.
        return string[-1] + formatar_string(string[:-1])


if frase_format == formatar_string(frase_format):
    print(f'A Frase: {frase} é Palidromo')
else:
    print(f'A Frase: {frase} não é Palindromo')

# Metodo 3 com Append() e Pop()

frase_lista = []
for i in frase:
    frase_lista.append(i)
nova_frase = ""
while frase_lista:
    nova_frase += frase_lista.pop()

nova_frase = nova_frase.replace(' ', '')


if frase_format == nova_frase:
    print(f'A Frase: {frase} é Palidromo')
else:
    print(f'A Frase: {frase} não é Palindromo')

# Metodo 4 com for varendo de traz pra frente

inverso = ''
for letra in range(len(frase_format) - 1, -1, -1):
    inverso += frase_format[letra]

if frase_format == inverso:
    print(f'A Frase: {frase} é Palidromo')
else:
    print(f'A Frase: {frase} não é Palindromo')
