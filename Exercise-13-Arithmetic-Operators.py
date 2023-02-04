# Exercicio resolvido por Cesar Augusto Numero 13 16/01/23
# Faça um algoritmo que leia o salário de um funcionario e mostre seu novo salário, com 15% de aumento

salario_antigo = float(input('Informe seu Salário atual: R$'))
salario_bonus = salario_antigo + (salario_antigo*15)/100
print(
    f'Seu Salário de R${salario_antigo :0.2f}Reais teve um bonus de 15% e agora vale R${salario_bonus :0.2f}Reais')
