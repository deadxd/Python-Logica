# Exercicio resolvido por Cesar Augusto Numero 76 24/01/23
# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequencia.
# no final, mostre uma listagem de preços, organizando os dados em forma de tabular.

produtos_e_precos = ('Arroz', 5, 'Feijão', 8.7,
                     'Macarão', 2.90, 'Leite em pó', 4.80)

for p in range(0, len(produtos_e_precos), 2):
    print(f'Produto é: {produtos_e_precos[p]}')
    print(f'Preco desse produto é: R${produtos_e_precos[p+1]}')
