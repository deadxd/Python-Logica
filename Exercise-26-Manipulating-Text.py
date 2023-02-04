# Exercicio resolvido por Cesar Augusto Numero 26 19/01/23
# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra 'A' - Em que posição ela aparece a primeira vez - em que posição ela aparece a ultima vez

frase = str(input('Informe uma frase para tratamento: ')).upper().strip()

frase_lenght = len(frase)

letra_count = frase.count('A')
print(f'A letra A aparece {letra_count} vezes')

letra_indice_first = frase.find('A')
print(
    f'A letra A aparece na posição {letra_indice_first} do index pela primeira vez')

letra_indice_last = frase.rfind('A')

print(
    f'A letra A aparece na posição {letra_indice_last} do index pela ultima vez')
