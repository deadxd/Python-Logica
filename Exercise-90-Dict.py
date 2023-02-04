# Exercicio resolvido por Cesar Augusto Numero 90 27/01/23
# Faça um programa que leia nome e média de um aluno guardando também a situação em um dicionario
# No final, mostre o conteúdo da estrutura na tela. Media > 7 Aprovado!

aluno = {}

aluno['nome'] = str(input('Informe seu nome: ')).upper().strip()
aluno['média'] = float(input('Informe sua Média: '))

if aluno['média'] >= 7:
    aluno['situação'] = 'APROVADO'
    #print(f'Situação: APROVADO!')
else:
    aluno['situação'] = 'RECUPERAÇÃO'


# Troca isso:
'''
print(f'Nome: {aluno["nome"]}')
print(f'Média: {aluno["média"]}')
print(f'Situação: {aluno["situação"]}')
'''
# Por isso:
for key, value in aluno.items():
    print(f'{key} : {value}')
