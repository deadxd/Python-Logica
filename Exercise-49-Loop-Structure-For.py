# Exercicio resolvido por Cesar Augusto Numero 49 21/01/23
# Refaça o desafio 09, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

numero_inteiro = int(input('Informe um numero inteiro qualquer: '))

print(f'{"=" :=>20}')
print(f'A tabuada do {numero_inteiro} é: ')
for i in range(1, 10+1):
    print(f'{numero_inteiro} X {i} = {numero_inteiro * i}')

print(f'{"=" :=>20}')
