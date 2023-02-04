# Exercicio resolvido por Cesar Augusto Numero 4 14/01/2023
# Faça um programa que leia 'algo' no teclado e informe seu Type e Classificação possiveis.

algo = input('Informe algo: ')

print('O tipo é: {} é alfa-númerico? {} é númerico? {} as letras são Maiusculas? {} são palavras? {}'.format(
    type(algo), algo.isalnum(), algo.isnumeric(), algo.isupper(), algo.isalpha()),)
