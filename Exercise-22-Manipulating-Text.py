# Exercicio resolvido por Cesar Augusto Numero 22 19/01/23
# Leia o nome completo de uma pessoa e mostre:
# O nome com todas as Letras Maiusculas - todas minusculas - quantas letras ao todo removendo espaços - quantas letras tem o primeiro nome
soma2 = 0
nome_completo = str(input('Informe seu nome completo: '))

# Seu nome em maisculo
print(nome_completo.upper())
# Seu nome em minusulo
print(nome_completo.lower())


# Quantas letras removendo todos espaços - METODO 1
nome_sem_espaco = len(nome_completo) - nome_completo.count(' ')

print(f'Seu nome tem ao todo {nome_sem_espaco} Letras')

# Quantas letras removendo todos espaços - METODO 2

# Virou uma lista e Quebrou Espaços
nome_completo_lista = nome_completo.split()

# Numero do index da nova LISTA
nome_completo_index = len(nome_completo_lista)

# Recebe o numero de listas e soma cada palavra sem conta o espaço.
for i in range(0, nome_completo_index):
    soma = len(nome_completo_lista[i])
    soma2 += soma

print(f'Seu nome tem ao todo {soma2} Letras')


# Index apenas do primeiro nome - METODO 1
print(f'Primeiro nome tem {len(nome_completo_lista[0])} Letras')

# Usando Find retorna tudo até o primeiro espaço - Metodo 2
print(f'Primeiro nome tem { nome_completo.find(" ") } Letras')
