# Exercicio resolvido por Cesar Augusto Numero 67 24/01/23
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido qunado o número solicitado for negativo

count = 0

numero = int(
    input('Informe valores inteiros ou [-] negativos para encerrar o programa: '))

if numero > 0:
    while True:
        count += 1
        if count < 10:
            print(f'{numero} x {count} = {numero * count}')
        else:
            numero = int(
                input('Informe valores inteiros ou [-] negativos para encerrar o programa: '))
            if numero > 0:
                count = 0
            else:
                break
print('Fim do programa')
