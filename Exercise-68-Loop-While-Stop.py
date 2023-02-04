# Exercicio resolvido por Cesar Augusto Numero 68 24/01/23
# Faça um programa que jogue par ou impar com o computador.
# O jogo será interrompido quando o jogaor PERDER, mostrando o número de vitorias consecultivas.

from random import randint

numero_computador = randint(1, 10)

count = 0
while True:
    numero = int(input('Informe um Valor: '))
    par_ou_impar = str(
        input('Infome se é PAR/IMPAR [P/I]: ')).strip().upper()[0]

    soma = numero + numero_computador

    if soma % 2 == 0 and par_ou_impar == 'P':
        print(f'Você venceu! \nVamos jogar novamente!')
        count += 1
    elif soma % 2 == 1 and par_ou_impar == 'I':
        print(f'Você venceu! \nVamos jogar novamente!')
        count += 1
    else:
        break
print(f'GAME OVER! Você venceu {count} vezes.')
