# Exercicio resolvido por Cesar Augusto Numero 31 19/01/23
# Desenvolva um programa que pergunte a distancia de uma viagem em KM E CALCULE O PREÇO DA passagem,
# cobrando R$0,50 por KM para viagens até 200KM e R$0,45 para viagens acima de 200KM

distancia_passagem = int(input('Informe a distancia percorrida da viagem: '))

print(f'O valor da passagém é: R${(distancia_passagem*0.50) :0.2f}' if distancia_passagem <=
      200 else f'O valor da passagem é: R${(distancia_passagem*0.45) :0.2f}')
