# Exercicio resolvido por Cesar Augusto Numero 19 18/01/23
# um professor quer sortear um dos seus quatro alunos para apagar o quadro. faça um programa que ajude ele, lendo o nome deles e escreven o nome do escolhido.
from random import choice

alunos = []

for i in range(4):
    alunos.append(str(input('Informe o nome dos alunos a ser sorteado: ')))

escolhido = choice(alunos)

print(f'O escolhido foi {escolhido}, {escolhido} vá limpar o quadro!')
