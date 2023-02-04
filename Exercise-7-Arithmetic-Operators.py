# Exercicio resolvido por Cesar Augusto Numero 7 16/01/23
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota_1 = float(input('Informe sua Primeira Nota: '))
nota_2 = float(input('Informe sua Segunda Nota: '))

media = (nota_1 + nota_2)/2

print(
    f'Baseando-se na sua Primeira Nota: {nota_1 :0.1f} e sua Segunda Nota: {nota_2 :0.1f} a média entre ela é: {media :0.1f}')

# Extra
if (media >= 7):
    print(f'Sua media foi: {media :0.1f}, Parabéns você foi Aprovado!')

else:
    print(f'Sua media foi: {media :0.1f}, Você reprovou, estude mais!')
