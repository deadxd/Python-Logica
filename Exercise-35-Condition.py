# Exercicio resolvido por Cesar Augusto Numero 35 19/01/23
# Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou não formar um triangulo

A = int(input('Informe o valor do reta A: '))  # EX: 5
B = int(input('Informe o valor do reta B: '))  # EX: 3
C = int(input('Informe o valor da reta C: '))  # EX: 10

AB = (A+B) > C  # BA = (B+A) > C #TRUE
AC = (A+C) > B  # CA = (C+A) > B #TRUE
BC = (B+C) > A  # CB = (C+B) > A #TRUE

print(AB)
print(AC)
print(BC)

# Metodo 1 IF e ELSE

if AB:
    if AC:
        if BC:
            print('Podem se forma um triangulo')
        else:
            print('Não podem se forma um triangulo')
    else:
        print('Não podem se forma um triangulo')
else:
    print('Não podem se forma um triangulo')

# Metodo 2 Operador AND

if AB and AC and BC:
    print('Podem se forma um triangulo')
else:
    print('Não podem se forma um triangulo')
