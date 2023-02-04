# Exercicio resolvido por Cesar Augusto Numero 93 27/01/23
# Crie um programa que gerencie o aporveitamento de um jogador de futebol.
# programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionario, incluindo o total de gols feitos durante o campeonato.

jogador = {}
num_gols = []
total_gols = 0

jogador['nome'] = str(input('Informe o nome do jogador: ')).upper().strip()
jogador['partidas'] = int(input('Informe quantas partidas jogou: '))

for indice in range(1, jogador['partidas']+1):
    gols = int(input(f'Informe número de gols na partida {indice}: '))
    total_gols += gols
    num_gols.append(gols)

jogador['gols'] = num_gols[:]
jogador['total'] = total_gols

print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
count = 1
for value in jogador['gols']:
    print(f'Na partida {count}, fez {value} gols.')
    count += 1

print(f'Foi um total de {jogador["total"]} gols.')
