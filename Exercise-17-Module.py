# Exercicio resolvido por Cesar Augusto Numero 17 18/01/23
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, caclcule e mostre o comprimento da hipotenusa.

from math import hypot

# Usando Math

cateto_oposto_math = int(input('Informe o cateto oposto do Triangulo: '))
cateto_adjacente_math = int(input('Informe o cateto adjacente do triangulo: '))

hipotenusa_math = hypot(cateto_oposto_math, cateto_adjacente_math)

print(f'O valor da hipotenusa dos catetos é: {hipotenusa_math}')

# Usando a Formula da hipotenusa

cateto_oposto_formula = int(input('Informe o cateto oposto do Triangulo: '))
cateto_adjacente_formula = int(
    input('Informe o cateto adjacente do triangulo: '))

hipotenusa_formula = (cateto_oposto_formula**2 +
                      cateto_adjacente_formula**2)**(1/2)

print(f'O valor da hipotenusa dos catetos é: {hipotenusa_formula}')
