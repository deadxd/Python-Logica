# Exercicio resolvido por Cesar Augusto Numero 72 24/01/23
# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de 0 até 20.
# O programa deverá ler um número pelo teclado entre 0 e 20 e mostra-lo por extenso.

numero_extenso = ('zero', 'um', 'dois', 'três', 'quatro',
                  'cinco', 'seis', 'sete', 'oito', 'nove',
                  'dez', 'onze', 'doze', 'treze', 'quatorze',
                  'quinze', 'dezesseis', 'dezessete', 'dezoito',
                  'dezenove', 'vinte')

numero = int(input(
    'Informe um número entre 0 e 20 para saber como se escreve por extenso: '))

while True:
    if 0 <= numero <= 20:
        print(f'O Número: {numero} por extenso é: {numero_extenso[numero]}')
        break
    else:
        numero = int(input('Insira um número entre 0 e 20: '))
