# Exercicio resolvido por Cesar Augusto Numero 11 16/01/23
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro equivale a uma area de 2m²

altura = float(input('Informe a Altura da parede em Metros: '))
largura = float(input('Informe a Largura da parede em Metros: '))

print(
    f'A area da parede é {(altura*largura) :0.2f}M² e são necessario {(altura*largura)/2 :0.2f} Litros de Tinta para pinta-la')
