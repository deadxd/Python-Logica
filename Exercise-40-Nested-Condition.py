# Exercicio resolvido por Cesar Augusto Numero 40 20/01/23
# Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final, de acordo com a media atingida:
# Media abaixo de 5.0: reprovado
# Media entre 5.0 e 6.9: Recuperação
# Media 7.0 ou superior: Aprovado

primeira_nota = float(input('Insira sua primeira nota: '))
segunra_nota = float(input('Insira sua segunda nota: '))

media = float(f'{(primeira_nota + segunra_nota) / 2 :0.1f}')

if media < 5:
    print(f'Com a media: {media} você está: Reprovado!')
elif 5 <= media <= 6.9:
    print(f'Com a media: {media} você está: Recuperação')
else:
    print(f'Com a media: {media} você está: Aprovado')
