# Exercicio resolvido por Cesar Augusto Numero 89 26/01/23
# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta
# no final, mostre um boletim contendo a media de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

lista_alunos = []
lista_aluno = []

while True:
    nome = str(input('Informe nome do aluno: '))
    nota_1 = float(input('Informe a primeira nota: '))
    nota_2 = float(input('Informe a segunda nota: '))
    media = (nota_1 + nota_2) / 2
    lista_aluno = [nome, nota_1, nota_2, media]
    lista_alunos.append(lista_aluno[:])

    perguntar = str(input('Deseja cadastrar mais aluno? [S][N]'))

    if perguntar in 'Nn':
        break
print('ID  NOME     MÉDIA')
print('='*50)
for aluno in range(0, len(lista_alunos)):
    print(f'{aluno}', end='   ')
    print(f'{lista_alunos[aluno][0]}', end='     ')
    print(f'{lista_alunos[aluno][-1]}')

while True:
    mostrar_notas = int(
        input('Mostra a nota de qual aluno? insira seu ID [999] interrompe: '))
    if mostrar_notas == 999:
        print('FIM DO PROGRAMA')
        break
    print(
        f'As notas de: {lista_alunos[mostrar_notas][0]} são: {lista_alunos[mostrar_notas][1:3]}\n')
