# Exercicio resolvido por Cesar Augusto Numero 50 21/01/23
# Desenvolva um programa que leia seis número inteiros e mostre a soma apenas daqueles que forem pares. se o valor digitado for impar desconsidere.
numero = 0
soma = 0
count = 0
for i in range(1, 7):
    numero = int(input(f'informe o {i} número inteiro: '))
    if numero % 2 == 0:
        soma += numero
        count += 1
print(
    f'Você informou {count} Números Pares e a soma de todos os pares é: {soma}')
