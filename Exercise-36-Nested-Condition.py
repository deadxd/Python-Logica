# Exercicio resolvido por Cesar Augusto Numero 36 20/01/23
# Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
# O programa vi perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar
# Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário
# Ou então o emprestimo será negado

import time

valor_imovel = int(input('Informe o valor do imovel: '))
salario = float(input('Informe seu Salário: '))
anos_pagamento = int(input('Informe em quantos anos quer parcelar: '))

parcelamento_mensal = valor_imovel / (anos_pagamento * 12)

limite_renda = (salario * 30) / 100

print(
    f'Financiamento de R$ {valor_imovel} em {anos_pagamento} anos com prestações de R$ {parcelamento_mensal :0.2f}')

print('VALIDANDO DADOS...')
time.sleep(2)

if parcelamento_mensal < limite_renda:
    print(f'Aprovado no Financiamento')
else:
    print(f'Reprovado no financiamento')
