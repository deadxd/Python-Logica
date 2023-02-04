# Exercicio resolvido por Cesar Augusto Numero 6 16/01/23
# Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada

numero = int(input('Insira um número: '))
print(
    f'Acessando o número: {numero} \nseu dobro é: {(numero *2)} \nseu triplo é: {(numero *3)} \ne sua raiz quadrada é: {(pow(numero,1/2))}')
# ou
print(
    f'Acessando o número: {numero} \nseu dobro é: {(numero *2)} \nseu triplo é: {(numero *3)} \ne sua raiz quadrada é: {(numero**(1/2))}')
