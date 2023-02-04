# Exercicio resolvido por Cesar Augusto Numero 47 21/01/23
# crie um programa que mostre na tela todos os números pares que estão no intervalo de 1 e 50

# Vai varrer começando do 1, mas com maior carga computacional
for pares in range(1, 50+1):
    print('.')
    if pares % 2 == 0:
        print(pares)

# Menor uso computacional
for pares in range(2, 51, 2):
    print('.')
    print(pares)
