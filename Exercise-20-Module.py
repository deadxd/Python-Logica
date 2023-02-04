# Exercicio resolvido por Cesar Augusto Numero 20 18/01/23
# Seguindo o Exercicio 19, o professor quer sortear a ordem de apresentação de trabalhos dos 4 alunos...

from random import choice, shuffle

alunos = []

for i in range(4):
    alunos.append(input('Informe o nome dos Alunos: '))


# Usando Shuffle e embaralhando

shuffle(alunos)

print(f'E a ordem de apresentação é: {alunos} ')

# Usando Choice e Removendo da lista

print(f'E a ordem nova ordem a apresentação é: ')
for i in range(4):
    aluno_sorteado = choice(alunos)

    print(f'{aluno_sorteado}')

    alunos.remove(aluno_sorteado)
