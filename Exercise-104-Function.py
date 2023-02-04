#Exercicio resolvido por Cesar Augusto Numero 104 30/01/23
    #Crie um programa que tenha uma função leiaInt(), que vai funcionar igual ao INPUT()
        #Só que fazendo a validação para aceitar apenas um valor númerico
        

def leiaInt(string):
    numeroInt = str(input(string))
    while numeroInt.isnumeric() != True:
        print(f'Erro! Digite um número inteiro válido.')
        numeroInt = str(input(string))
    return numeroInt

n = leiaInt('Digite um número: ')
print(f'Você digitou o número: {n}')