# Exercicio resolvido por Cesar Augusto Numero 92 27/01/23
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionario
# se por acaso a CTPS for diferente != de 0 o dicionario receberá também o ano de contratação e o salário.
# calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
# 35 anos de serviço se aposenta.

from datetime import date

ano_atual = date.today().year
pessoa = {}

pessoa['nome'] = str(input('Informe seu nome: ')).strip().upper()
ano_de_nascimento = int(input('Informe ano de nascimento: '))
pessoa['idade'] = ano_atual - ano_de_nascimento
pessoa['CTPS'] = int(input('Informe CTPS, informe 0 se não tiver CTPS: '))

if pessoa['CTPS'] != 0:
    pessoa['Ano de Contratação'] = int(
        input('Informe o ano que foi contratado: '))
    pessoa['salario'] = float(input('Informe seu salario: '))
    pessoa['aposentadoria'] = pessoa['idade'] + \
        (35 - (ano_atual - pessoa['Ano de Contratação']))


for key, value in pessoa.items():
    print(f'{key} : {value}')
