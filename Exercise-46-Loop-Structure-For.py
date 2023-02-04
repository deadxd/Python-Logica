# Exercicio resolvido por Cesar Augusto Numero 46 21/01/23
# Faça um programa que mostre na tela uma contagem regressiva para o ano novo,  indo de 10 a 0, com uma pausa de 1 segundo entre eles.

from time import sleep

hora = '23:59:30'

for contagem_hora in range(int(hora[6:]), 50, 1):
    print(f'Hora atual é: {hora[0:5]}:{contagem_hora}')
    sleep(1)

for contagem_regressiva in range(10, -1, -1):
    print(f'Faltam {contagem_regressiva} segundos para o ano novo.')
    sleep(1)
print('Feliz Ano Novo!')
