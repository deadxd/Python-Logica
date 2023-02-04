#Exercicio resolvido por Cesar Augusto Numero 106 30/01/23
    #Faça um mini-sistema que utilize o interactive Help, O usuário vai digitar o comando e o manual vai aparecer.
        #Quando o usuário digitar a palavra 'FIM' o programa se encerrará.

def leiaInt(string):
    func = str(input(string))
    if func != 'fim':   
        return help(func)
    else:
        return 'fim'

while True:
    if leiaInt('Função ou Biblioteca > ') != 'fim':
        func = leiaInt('Função ou Biblioteca > ')
        print(func)
    else:
        print('FIM DO PROGRAMA!')
        break