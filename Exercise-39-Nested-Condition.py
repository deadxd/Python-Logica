# Exercicio resolvido por Cesar Augusto Numero 39 20/01/23
# faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento.
# Mostrar o tempo que falta ou se passou do prazo.
from datetime import date

ano_atual = date.today().year

ano_nascimento = int(input('Informe o ano que nasceu: '))

idade = ano_atual - ano_nascimento

if 18 <= idade <= 24:
    print(f'Você tem {idade} anos, já pode fazer o alistamento militar')
elif idade < 18:
    print(
        f'Você tem {idade} anos, não pode ainda fazer o alistamento militar faltam {-(idade - 18)} anos para se alistar')
else:
    print(f'Você tem {idade} anos, já passou do periodo de alistamento, você deveria ter se alistado há {idade - 18} anos sinto muito!')
