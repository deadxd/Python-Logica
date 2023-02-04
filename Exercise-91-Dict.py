# Exercicio resolvido por Cesar Augusto Numero 91 27/01/23
# Crie um programa onde 4 jogadores joguem um dado e tenham resultado aleatórios
# Guarde esses resultados em um DICIONARIO. no final coloque esse DICIONARIO em ordem
# Sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogo = {}

for c in range(1, 5):
    jogo[f'jogador{c}'] = randint(1, 6)

for key, value in jogo.items():
    print(f'O {key} tirou {value}')
    sleep(0.5)

print(f'Ranking dos jogadores: ')

# Dificuldade em sabe qual o segundo parametro para passar.
# item[1] faz com valores e item[0] faz com as chaves
# Novo python 3.7+ cpython 3.6
#jogo_ordenado = dict(sorted(jogo.items(), key=lambda item: item[1], reverse=True))

# Velho python
jogo_ordenado = dict(sorted(jogo.items(), key=itemgetter(1), reverse=True))

count = 1
for key, value in jogo_ordenado.items():
    print(f'{count}ª lugar: {key} com {value}')
    count += 1
    sleep(0.5)
