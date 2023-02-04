# Exercicio resolvido por Cesar Augusto Numero 81 25/01/23
# Crie um programa que vai ler vários números e colocar em uma lista depois disso mostre:
# A)Quantos números foram digitados.
# B)A lista de valores, ordenada de forma decrescente.
# C)Se o valor 5 foi digitado e está ou não na lista.

numeros = []
resposta = 'S'
count = 0
boleano = False

while resposta == 'S':
    numeros.append(int(input('Infome um número inteiro: ')))
    resposta = str(input('deseja continuar? [S][N]: ')).strip().upper()
    count += 1

numeros.sort(reverse=True)
print(
    f'A quantidade de números digitados foram: {count} \nLista em ordem decrecente: {numeros}\n')
if 5 in numeros:
    print(f'O número 5 faz parte da lista!')
else:
    print(f'O número 5 não faz parte da lista!')
