# Exercicio resolvido por Cesar Augusto Numero 33 19/01/23
# faça um programa que leia três numeros e mostre qual é o maior e qual é o menor

primeiro_numero = int(input('Insira 1ª número: '))
segundo_numero = int(input('Insira 2ª número: '))
terceiro_numero = int(input('Insira 3ª número: '))

# Metodo 1 usando if e else

if primeiro_numero > segundo_numero:
    if primeiro_numero > terceiro_numero:
        print(f'Maior numero é o Primeiro')
        if segundo_numero > terceiro_numero:
            print(f'O menor numero é o Terceiro')
        else:
            print(f'O menor numero é o Segundo')

if segundo_numero > primeiro_numero:
    if segundo_numero > terceiro_numero:
        print(f'Maior numero é o Segundo')
        if primeiro_numero > terceiro_numero:
            print(f'O menor numero é o Terceiro')
        else:
            print(f'O menor numero é Primeiro')

if terceiro_numero > primeiro_numero:
    if terceiro_numero > segundo_numero:
        print(f'Maior numero é o Terceiro')
        if primeiro_numero > segundo_numero:
            print(f'O menor numero é o Segundo')
        else:
            print(f'O menor numero é Primeiro')

# Metodo 2 - usando função existente

lista_numero = [primeiro_numero, segundo_numero, terceiro_numero]

maior = max(lista_numero)
menor = min(lista_numero)

print(f'O maior número é: {maior} e menor número é: {menor}')

# Metodo 3 - usando operador and

menor_3 = primeiro_numero

if segundo_numero < primeiro_numero and segundo_numero < terceiro_numero:
    menor_3 = segundo_numero
if terceiro_numero < primeiro_numero and terceiro_numero < segundo_numero:
    menor_3 = terceiro_numero

maior_3 = primeiro_numero
if segundo_numero > primeiro_numero and segundo_numero > terceiro_numero:
    maior_3 = segundo_numero
if terceiro_numero > primeiro_numero and terceiro_numero > segundo_numero:
    maior_3 = terceiro_numero

print(f'O maior número é: {maior} e menor número é: {menor}')
