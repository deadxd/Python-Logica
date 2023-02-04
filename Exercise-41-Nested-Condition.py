# Exercicio resolvido por Cesar Augusto Numero 41 20/01/23
# Leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade:
# Ate 9 anos: MIRIM
# Ate 14 anos: INFANTIL
# Ate 19 anos: JUNIOR
# Ate 20 Anos: SENIOR
# ACIMA de 20: MASTER

from datetime import date

ano_atual = date.today().year

ano_nascimento = int(input('Insira seu ano de nascimento: '))

idade = ano_atual - ano_nascimento

if idade <= 9:
    print(f'Com {idade} anos sua categoria é: MIRIM')
elif idade <= 14:
    print(f'Com {idade} anos sua categoria é: INFANTIL')
elif idade <= 19:
    print(f'Com {idade} anos sua categoria é: JUNIOR')
elif idade == 20:
    print(f'Com {idade} anos sua categoria é: SENIOR')
else:
    print(f'Com {idade} anos sua categoria é: MASTER')
