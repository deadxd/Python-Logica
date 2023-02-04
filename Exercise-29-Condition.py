# Exercicio resolvido por Cesar Augusto Numero 29 19/01/23
# Escreva um programa que leia a velocidade de um carro, se ultrapassar 80km/h mostra uma multa, a multa vai custa R$7 por cada km aima do limite

carro_velocidade = int(input('Informe a velocidade do carro: '))
calculo_multa = (carro_velocidade - 80)*7
print(f'A multa equivale a: R${calculo_multa} Reais' if carro_velocidade >
      80 else 'Não houve multa!')
