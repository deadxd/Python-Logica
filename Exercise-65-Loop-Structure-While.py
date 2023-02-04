# Exercicio resolvido por Cesar Augusto Numero 65 23/01/23
# crie um programa que leia vários números inteiros pelo teclado.
# no final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor valore lido.
# o programa deve perguntar ao usuario se ele quer ou não continuar a digitar valores.

perguntar = 'S'
#count = 0
media = soma_numeros = maior_numero = menor_numero = count = 0
#soma_numeros = 0
#maior_numero = 0
#menor_numero = 0

while perguntar in 'Ss':
    numero = int(input('Informe número inteiro: '))
    perguntar = str(
        input('Deseja encerrar o programa? [S] [N]: ')).strip().upper()[0]
    count += 1
    soma_numeros += numero
    # Setar o valor do maior e do menor
    if count == 1:
        maior_numero = numero
        menor_numero = numero
    else:
        # Qual é o maior número
        if maior_numero < numero:
            maior_numero = numero
        else:
            # Qual é o menor número
            menor_numero > numero
            menor_numero = numero
    if perguntar != 'S' and perguntar != 'N':
        #perguntar = str(input('Programa só aceita [S] [N] tente novamente: ')).strip().upper()
        perguntar = 'S'

media = soma_numeros / count

print(
    f'A media entre todos valores é: {media} o maior valor foi {maior_numero} e o menor foi {menor_numero}')
