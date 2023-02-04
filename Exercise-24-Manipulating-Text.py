# Exercicio resolvido por Cesar Augusto Numero 24 19/01/23
# Crie um programa que leia o nome de uma cidade e diga se ela começa com ou não o nome 'Santo'

cidade = str(input('Informe o nome de uma cidade: '))

cidade_lenght = len(cidade)

# Validacao nome Cidade tem que existir
while cidade_lenght < 1:
    cidade = input('Erro: Informe o nome de uma cidade: ')
    cidade_lenght = len(cidade)

cidade_lista = cidade.upper().split()

# Metodo 1

cidade_bool = 'SANTO' in cidade_lista[0]

print(f'A cidade {cidade} comeca com Santo? {cidade_bool} ')

# Metodo 2 - Traduzindo True ou False

if cidade_lista[0] == 'SANTO':
    print(f'A Cidade: {cidade} começa com Santo')
else:
    print(f'A Cidade: {cidade} não começa com Santo')

# Metodo 3 - Com Strip e Fatiamento = Range

cidade2 = str(input('Informe o nome de uma cidade: ')).strip()
print(f'A Cidade {cidade2} comeca com Santo? {cidade2[:5].upper() == "SANTO"}')
