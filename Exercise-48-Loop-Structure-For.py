# Exercicio resolvido por Cesar Augusto Numero 48 21/01/23
# faça um programa que calcule a soma entre todos os números impares que são multiplos de três e que se encontram no intervalo de 1 até 500

soma = 0

# Pulando de 2 em 2 para remover os pares e somar os impares
for impares in range(1, 500+1, 2):
    if impares % 3 == 0:
        print(impares)
        soma += impares

print(soma)
