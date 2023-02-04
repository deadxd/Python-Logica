# Exercicio resolvido por Cesar Augusto Numero 95 27/01/23
# Aprimore o Exercicio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualizalão de detalhe do aproveitamento de cada jogador.

jogador = {}
jogadores = []
num_gols = []
total_gols = 0
count_id = 0

while True:
    jogador['ID'] = count_id
    jogador['nome'] = str(input('Informe o nome do jogador: ')).upper().strip()
    jogador['partidas'] = int(input('Informe quantas partidas jogou: '))

    for indice in range(1, jogador['partidas']+1):
        gols = int(input(f'Informe número de gols na partida {indice}: '))
        total_gols += gols
        num_gols.append(gols)

    jogador['gols'] = num_gols[:]
    jogador['total'] = total_gols
    num_gols.clear()
    jogadores.append(jogador.copy())

    perguntar = str(input('Deseja continuar? [S][N] '))

    if perguntar in 'Nn':
        break

    count_id += 1

print(f'ID  NOME           GOLS          TOTAL')
for c in range(0, len(jogadores)):
    print(
        f'{jogadores[c]["ID"]}   {jogadores[c]["nome"]}   {jogadores[c]["gols"]}     {jogadores[c]["total"]}')

#print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')

#print(f'Foi um total de {jogador["total"]} gols.')


while True:
    num_jogador = int(
        input('Mostrar dados de qual jogador? [999] pra parar: '))
    print(f'Levantamento do jogador {jogadores[num_jogador]["nome"]}: ')
    print()
    count = 1
    for value in jogadores[num_jogador]['gols']:
        print(f'Na partida {count}, fez {value} gols.')
        count += 1

    if num_jogador == 999:
        break
