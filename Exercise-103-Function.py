#Exercicio resolvido por Cesar Augusto Numero 103 30/01/23
    #Faça um programa que tenha uma função chamada ficha(), que receba 2 parametros:
    #1)Nome de um joador
    #2)Quantos gols ele marcou
        #O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome=0, gols=0):
    nome_local = '<desconhecido>'
    gols_local = 0
    if nome == '' and gols == '':
        print(f'O jogador {nome_local} fez {gols_local} gol(s) no campeonato.')
    elif nome != '' and gols != '':
        print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
    elif nome == '':
        print(f'O jogador {nome_local} fez {gols} gol(s) no campeonato.')
    else:
        print(f'O jogador {nome} fez {gols_local} gol(s) no campeonato.')
        
nome = str(input('Informe o nome do jogador: ')).strip().upper()
gols = str(input('Informe número de gols marcados: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

ficha(nome, gols)