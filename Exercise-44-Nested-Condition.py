# Exercicio resolvido por Cesar Augusto Numero 44 20/01/23
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# A vista dinheiro/cheque: 10% de desconto
# A vista no Cartão: 5% de desconto
# Parcelado em 2x no cartão: Preço Normal
# Parcelado em 3x ou + no cartão: 20% de Juros

preco_compra = float(input('Informe o valor da compra: '))
forma_pagamento = int(input(
    'Insira 1: Pagamento Dinheiro/Cheque com 10% Desconto \nInsira 2: Cartão Avista com 5% De desconto \nInsira 3: Parcelado em 2x Sem juros \nInsira 4: Parcelado 3x ou mais com 20% De juros \n'))

if forma_pagamento == 1:
    print(
        f'O valor da compra agora é: R${preco_compra - (preco_compra*10) / 100}')
elif forma_pagamento == 2:
    print(
        f'O valor da compra agora é: R${preco_compra - (preco_compra*5) / 100}')
elif forma_pagamento == 3:
    print(f'O valor da compra agora é: 2x de: R${preco_compra / 2}')
elif forma_pagamento == 4:
    numero_parcelas = float(input('Informe em quantas vezes que parcelar: '))
    print(
        f'O valor da compra agora é: {numero_parcelas}x de R${(preco_compra + (preco_compra*20) / 100) / numero_parcelas} com Juros')
else:
    print('Opcao invalida de pagamento tente novamente!')
