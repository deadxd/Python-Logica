# Exercicio resolvido por Cesar Augusto Numero 23 19/01/23
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
# ex: 3945 unidade: 5 - dezena: 4 - centena: 9 - milhar: 3

numero = input('Informe um numero entre 0 e 9999: ')

numero_lenght = len(numero)

# Validacao - Enquanto não for menor que 9999.... retorna e atualiza o lenght
while numero_lenght > 4:
    numero = input('Erro: Informe um numero entre 0 e 9999: ')
    numero_lenght = len(numero)

# Para cada tipo de lenght um tipo de unidade
if numero_lenght == 1:
    print(f'Unidade é: {numero[0]}')
elif numero_lenght == 2:
    print(f'Unidade é: {numero[1]}')
    print(f'Dezena é: {numero[0]}')
elif numero_lenght == 3:
    print(f'Unidade é: {numero[2]}')
    print(f'Dezena é: {numero[1]}')
    print(f'Centena é: {numero[0]}')
elif numero_lenght == 4:
    print(f'Unidade é: {numero[3]}')
    print(f'Dezena é: {numero[2]}')
    print(f'Centena é: {numero[1]}')
    print(f'Milhar é: {numero[0]}')

# Metodo 2 simples usando matematica

numero_int = int(numero)

# EX: 1357 // 1 = 1357 | 1357 % 10 = 7
unidade = numero_int // 1 % 10

# EX: 1357 // 10 = 135 | 135 % 10 = 5
dezena = numero_int // 10 % 10

# EX: 1357 // 100 = 13  |  13 % 10 = 3
centena = numero_int // 100 % 10

# EX: 1357 // 1000 = 1 | 1 % 10 = 1
milhar = numero_int // 1000 % 10

print(f'Unidade é: {unidade}')
print(f'Dezena é: {dezena}')
print(f'Centena é: {centena}')
print(f'Milhar é: {milhar}')
