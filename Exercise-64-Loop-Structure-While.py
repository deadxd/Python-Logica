# Exercicio resolvido por Cesar Augusto Numero 64 23/01/23
# Crie um programa que leia vários números inteiro pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles. (desconsiderando o flag)

numero = 0
soma = 0
count = 0

while numero != 999:
    numero = int(
        input('Informe um número inteiro qualquer ou 999 para parar o programa: '))
    if numero != 999:
        soma += numero
        count += 1
print(
    f'Fim do programa, foram digitados {count} números e a soma de todos os números digitados foi {soma}')
