# Exercicio resolvido por Cesar Augusto Numero 18 18/01/23
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

angulo = int(input('Infome um Angulo de 1 a 360º: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(
    f'Baseado no angulo informado: {angulo}º seu seno é: {seno :.2f} seu cosseno é: {cosseno :.2f} e sua tangente é {tangente :.2f}')
