# Exercicio resolvido por Cesar Augusto Numero 34 19/01/23
# escreva um programa que pergunte o salário de um funcionario e calcule o valor do seu aumento.
# Pra salários superires a R$1250, calcule um aumento de 10%.
# Pra salários inferires ou iguais a R$1250 aumento de 15%.

salario = float(input('Informe seu salário para o aumento: '))
print(f'Seu novo salário é: {(salario*15)/100 + salario :0.2f}' if salario <=
      1250 else f'Seu novo salário é: {(salario*10)/100 + salario :0.2f}')
