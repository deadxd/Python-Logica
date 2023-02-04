#Exercicio Facil resolvido por Cesar Augusto Numero 97 28/01/23
    #Faça um programa que tenha uma função chamada escreva()
        #que receba um texto qualquer como parametro e mostre uma mensagem com tamanho e bordas adaptaveis.

def escreva(msg):
    tamanho = len(msg) + 4
    print('~'* tamanho)
    print(f'  {msg}')
    print('~'* tamanho)


escreva('Como você esta?')
escreva('Cesar Augusto')