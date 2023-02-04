# Exercicio resolvido por Cesar Augusto Numero 61 23/01/23
# refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.


termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão do termo: '))
count = 0

while count != 10:
    print(termo, end=' ')
    termo += razao
    count += 1
