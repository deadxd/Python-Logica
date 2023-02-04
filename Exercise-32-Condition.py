# Exercicio resolvido por Cesar Augusto Numero 32 19/01/23
# Faça um programa que leia um ano qualquer e mostre se é bissexto

from datetime import date

ano = int(input('Informe um ano para saber se é Bissexto: '))

if ano == 0:
    ano = date.today().year

# Metodo 1

bissexto = ano % 4
bissexto_multiplo_100 = ano % 100
bissexto_multiplo_400 = ano % 400

if bissexto == 0:
    if bissexto_multiplo_100 == 0:
        if bissexto_multiplo_400 != 0:
            print(f'O ano: {ano} Não é Bissexto')
        else:
            print(f'O ano: {ano} é bissexto')
    else:
        print(f'O ano: {ano} é bissexto')
else:
    print(f'O ano: {ano} Não é Bissexto')

# Metodo 2

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano: {ano} é bissexto')
else:
    print(f'O ano: {ano} Não é Bissexto')
