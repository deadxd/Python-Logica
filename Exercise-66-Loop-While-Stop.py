# Exercicio resolvido por Cesar Augusto Numero 66 24/01/23
# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999
# Mostre quantos números foram digitados e qual foi a soma entre eles, desconsiderando a flag e usando condição de parada Break;

count = 0
soma = 0

while True:
    numero = int(input('Informe um número inteiro ou [999] para parar: '))
    if numero == 999:
        break
    count += 1
    soma += numero

print(f'Foram digitados: {count} e a soma entre eles foi {soma}')
