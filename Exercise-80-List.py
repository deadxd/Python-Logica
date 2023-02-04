# Exercicio resolvido por Cesar Augusto Numero 80 25/01/23
# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção
# Não use o sort()
# No final mostre a lista ordenada na tela.

numeros = []

for valores in range(0, 5):
    validador = int(input('Informe números inteiros: '))

    if valores == 0 or validador > numeros[-1]:
        numeros.append(validador)
    else:
        pos = 0  # posição não recebe um valor fixo, toda vez que roda ele vira 0, esse é o segredo
        print(pos)
        while pos < len(numeros):  # [0][1][2][3][4]
            if validador <= numeros[pos]:  # [1][8][9]
                print(numeros[pos])
                numeros.insert(pos, validador)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1

print(numeros)
