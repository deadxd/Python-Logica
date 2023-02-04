# Exercicio resolvido por Cesar Augusto Numero 63 23/01/23
# escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de fibonacci.

fibo_1 = 0
fibo_2 = 1

count = 0
fibonacci = int(input('Informe de qual número vc quer a fibonnaci: '))
fibonacci_fixo = fibonacci

# Metodo 1

while count != fibonacci_fixo - 1:
    if count == 0:
        print(fibo_1, end=' ')
    count += 1

    if count == 1:
        fibonacci = fibo_1 + fibo_2
        print(fibonacci, end=' ')
    else:
        fibonacci_fixo_soma = fibonacci
        fibonacci = fibonacci + fibo_2
        fibo_2 = fibonacci_fixo_soma
        print(fibo_2, end=' ')

# Metodo 2 /   0 - 1 - 1 - 2 - 3 - 5 - 8

termo_1 = 0
termo_2 = 1

print(f'\n{termo_1} {termo_2}', end=' ')
contador = 3
while contador <= fibonacci_fixo:
    termo_3 = termo_1 + termo_2
    print(f'{termo_3}', end=' ')
    termo_1 = termo_2
    termo_2 = termo_3
    contador += 1

print('\n')
# Metodo 3 eficiente

num = 1
a = 0
b = 1

while num <= fibonacci_fixo:
    print(f'{a}', end=' ')  # 0 1 1 2 3 5 . . .
    c = a + b  # 8
    a = b  # 5
    b = c  # 8
    num += 1

print('\nFIM')
