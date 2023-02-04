# Exercicio resolvido por Cesar Augusto Numero 28 19/01/23
# Faça o computador 'pensar' em um número inteiro de 0 a 5 e peça para o usuario tentar descobrir qual foi o número escolhido pelo computador
# Escreva na tela se acertou ou errou

from random import randint
from time import sleep

print('='*50)
print('Vou pensar em um número de 0 a 5. Tente Adivinhar...')
print('='*50)

# Sortear ente 0 e 5
numero_random = randint(0, 5)

numero_escolhido = int(input('Qual número eu pensei? '))

print('LOADING...')
sleep(2)

print('Você Acertou' if numero_random == numero_escolhido else 'Errou')
