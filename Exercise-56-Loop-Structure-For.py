# Exercicio resolvido por Cesar Augusto Numero 56 21/01/23
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. no final do programa, mostre:
# A media de idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres têm menos de 20 anos

idade_soma = 0
nome_lista = []
idade_lista = []
sexo_lista = []
qnt_mulheres_menores = 0
maior_idade = 0
nome_velho = ''

for i in range(1, 5):
    print(f'Informe {i} Vez(es) o(s) dado(s) da(s) pessoa(s).')
    nome = str(input('Informe seu nome: ')).strip()
    nome_lista.append(nome)
    idade = int(input('Informe sua idade: '))
    idade_lista.append(idade)
    sexo = str(input('Informe seu sexo: M ou F: ')).strip().upper()
    sexo_lista.append(sexo)

    idade_soma += idade
# Quantas mulheres tem menos de 20 anos
    if idade < 20 and sexo == 'F':
        qnt_mulheres_menores += 1

# Metodo 1 pegando a idade do mais velho e acessado index
    if idade > maior_idade and sexo == 'M':
        maior_idade = idade
        nome_velho = nome

nome_mais_velho = idade_lista.index(maior_idade)

# Calculo da Media da idade
idade_media = idade_soma / 4

# Metodo 2 - Nome do mais velho com lista
idade_lista_2 = idade_lista[:]
while len(idade_lista_2) != 1:
    if idade_lista_2[-1] > idade_lista_2[-2]:
        maior_idade = idade_lista_2[-1]
        idade_lista_2.remove(idade_lista_2[-2])
    else:
        maior_idade = idade_lista_2[-2]
        idade_lista_2.remove(idade_lista_2[-1])

nome_mais_velho_2 = idade_lista.index(maior_idade)


# Resultados

print(f'A media de idade é: {idade_media :0.0f} anos')

print(
    f'O nome do mais velho é: {nome_lista[nome_mais_velho]} ou {nome_velho}')

print(
    f'O número de mulheres com idade abaixo de 20 anos é: {qnt_mulheres_menores}')
