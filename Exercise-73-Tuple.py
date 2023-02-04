# Exercicio resolvido por Cesar Augusto Numero 73 24/01/23
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. e mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times de ordem alfabética.
# D) Em que posição na tabela está o time da Bragantino.
# Obs: lista tabela brasileirao ANO 2022
time_brasileirao = (
    'Palmeiras',
    'Internacional',
    'Fluminense',
    'Corinthians',
    'Flamengo',
    'Athletico-PR',
    'Atlético-MG',
    'Fortaleza',
    'São Paulo',
    'América-MG',
    'Botafogo',
    'Santos',
    'Goiás',
    'Bragantino',
    'Coritiba',
    'Cuiabá',
    'Ceará',
    'Atlético-GO',
    'Avaí',
    'Juventude')

print('='*100)
print(f'A Lista do brasileira é: {time_brasileirao}'.replace("'", ""))
print('='*100)
print(
    f'Os 5 primeiros colocados são: {time_brasileirao[0:5]}'.replace("'", ""))
print('='*100)
print(
    f'Os últimos 4 colocados da tabela são: {time_brasileirao[-4:]}'.replace("'", ""))
print('='*100)
print(f'A lista do brasileirão em ordem alfabetica é: {sorted(time_brasileirao)}'.replace(
    "'", ""))
print('='*100)
print(
    f'O time do Bragantino ta na posição: {time_brasileirao.index("Bragantino") + 1}')
print('='*100)
