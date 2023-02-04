# Exercicio resolvido por Cesar Augusto Numero 43 20/01/23
# Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# ABAIXO DE 18.5: ABAIXO DO PESO
# ENTRE 18.5 E 25: PESO IDEAL
# 25 ATE 30: SOBREPESO
# 30 ATE 40: OBESIDADE
# ACIMA DE 40: OBESIDADE MORBIDA

peso = int(input('Infome seu peso: '))
altura = float(input('Informe sua altura: '))

IMC = float(f'{peso / (altura**2) :0.2f}')

if IMC < 18.5:
    print(f'Com IMC de: {IMC}, você está: ABAIXO DO PESO')
elif 18.5 <= IMC <= 25:
    print(f'Com IMC de: {IMC}, você está: PESO IDEAL')
elif 25 < IMC <= 30:
    print(f'Com IMC de: {IMC}, você está: SOBREPESO')
elif 30 < IMC <= 40:
    print(f'Com IMC de: {IMC}, você está: OBESIDADE')
else:
    print(f'Com IMC de: {IMC}, você está: OBESIDADE MORBIDA')
