#Exercicio resolvido por Cesar Augusto Numero 101 30/01/23
    #Crie um programa que tenha uma função chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa, 
    # retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições

ano_de_nascimento = int(input('Informe o ano de nascimento: '))
idade = 0

def voto(ano_de_nascimento):
    from datetime import date
    global idade
    idade = date.today().year - ano_de_nascimento
    
    if idade < 16:
        valor_literal = 'Voto Negado!'
    elif idade < 65:
        valor_literal = 'Voto Obrigatorio!'
    else:
        valor_literal = 'Voto Opcional!'
    return valor_literal


votar = voto(ano_de_nascimento)

print(f'Com {idade} anos: {votar}')