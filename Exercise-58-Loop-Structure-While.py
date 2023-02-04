# Exercicio resolvido por Cesar Augusto Numero 58 23/01/23
# Refaça o desafio 28, só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
# Numeros entre 0 e 10

from random import randint
from time import sleep

print('='*50)
print('Vou pensar em um número de 0 a 10. Tente Adivinhar...')
print('='*50)

# Sortear ente 0 e 5
numero_random = randint(0, 10)

contador = 0

numero_escolhido = int(input('Qual número eu pensei? '))
contador += 1

print('LOADING...')
sleep(1)

while numero_random != numero_escolhido:
    contador += 1
    numero_escolhido = int(input('Você errou tente novamente entre 0 e 10? '))
    print('LOADING...')
    sleep(0.5)

print(f'Voce acertou depois de {contador} tentativas, parabéns !')
