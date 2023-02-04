# Exercicio resolvido por Cesar Augusto Numero 42 20/01/23
# Refaça o desafio 35 e acrecentando o recurso de mostra que tipo de triangulo sera formado:
# Equilatero: todos os lados iguais
# Isosceles: dois laos iguais
# Escaleno: todos os lados diferentes

A = int(input('Informe o valor do reta A: '))  # EX: 5
B = int(input('Informe o valor do reta B: '))  # EX: 3
C = int(input('Informe o valor da reta C: '))  # EX: 4

AB = (A+B) > C  # BA = (B+A) > C #TRUE
AC = (A+C) > B  # CA = (C+A) > B #TRUE
BC = (B+C) > A  # CB = (C+B) > A #TRUE

if AB and AC and BC:
    #print('Podem se forma um triangulo')
    if A == B == C:
        print(f'Esse é um triangulo Equilatero A = {A} B = {B} C = {C}')
    elif A == B or A == C or B == C:
        print(f'Esse é um triangulo Isosceles A = {A} B = {B} C = {C}')
    else:
        print(f'Esse é um triangulo Escaleno A = {A} B = {B} C = {C}')
else:
    print('Não podem se forma um triangulo')
