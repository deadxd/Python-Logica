# Exercicio resolvido por Cesar Augusto Numero 15 17/01/23
# Escreva um programa que pergunte a quantidade de Km rodados, quantidade de dias que foi alugado e calcule o preço a pagar. Diaria R$60 KM rodado R$0.15

dias_rodado = int(input('Informe Quantos dias o carro foi alugado: '))
km_rodado = float(input('Quantos KM o carro rodou durante todo percurso ?'))

diaria_carro_preco = float(60)
km_rodado_preco = float(0.15)

print(f'O carro foi alugado por {dias_rodado}Dias e Percorreu {km_rodado}KM, Custando assim {(diaria_carro_preco*dias_rodado) + (km_rodado*km_rodado_preco) :0.1f}Reais')
