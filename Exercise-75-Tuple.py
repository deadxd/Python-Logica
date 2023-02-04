# Exercicio resolvido por Cesar Augusto Numero 75 24/01/23
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla, e mostre:
# A) quantas vezes apareceu o valor 9.
# B)Em que posição foi digitado o primeiro valor 3.
# C)Quais foram os números pares.

numero = ()
numero_par = ()
count_9 = 0

for c in range(0, 4):
    input_1 = int(input('Informe um número: '))
    numero += (input_1,)
    if input_1 == 9:
        count_9 += 1
    if input_1 % 2 == 0:
        numero_par += (input_1,)

print(f'O número 9 apareceu: {count_9} x\n')

# outro jeito de achar o número 3:  'if 3 in numero:'
print(f'Posição do primeiro valor 3: {numero.index(3)+1}ª' if numero.count(
    3) > 0 else 'O numéro 3 não apareceu nenhuma vez')
print(f'Esses foram todos números pares: {numero_par}')
