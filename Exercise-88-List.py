# Exercicio resolvido por Cesar Augusto Numero 88 26/01/23
# Faça um programa que ajude um jogador da Mega Sena a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# Cadastrando tudo em uma lista composta.
import random
from time import sleep

num_lista = []
num_jogos = int(input('Quantos jogos deseja que eu sorteie? '))

for n_jogos in range(0, num_jogos):
    num_lista.append(random.sample(range(1, 60), 6))

    print(f'Jogo {n_jogos+1}: {num_lista[n_jogos]}')
    sleep(0.5)
