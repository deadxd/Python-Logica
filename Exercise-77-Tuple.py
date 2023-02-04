# Exercicio resolvido por Cesar Augusto Numero 77 24/01/23
# Crie um programa que tenha uma tupla com vários palavras (sem acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as sua vogais. A E I O U

palavras = ('ola', 'mundo', 'cesar', 'como', 'vai',
            'voce', 'hoje', 'paralalepipedo')

tamanho = len(palavras)

for p in range(0, tamanho):
    print(f'\nA palavra tem: {palavras[p]} tem as vogais: ', end='')
    for letra in range(0, len(palavras[p])):
        # if letra in 'aeiou':
        #print('letra', end=' ')
        if 'a' in palavras[p][letra]:
            print('a', end=' ')
        if 'e' in palavras[p][letra]:
            print('e', end=' ')
        if 'i' in palavras[p][letra]:
            print('i', end=' ')
        if 'o' in palavras[p][letra]:
            print('o', end=' ')
        if 'u' in palavras[p][letra]:
            print('u', end=' ')
