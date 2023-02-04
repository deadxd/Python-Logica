#Exercicio resolvido por Cesar Augusto Numero 102 30/01/23
    #Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
    #1) número a calcular
    #2) show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial

def fatorial(num, show=0):
    '''
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado
    :param show: (opcional) Mostra ou não a contagem
    :return: O valor do calculo do Fatorial
    '''
    for c in range(num, 0, -1):
        if show != 0:
            if c > 1:
                print(f'{c} X', end=' ')
            if c == 1:
                print(f'{c} =', end=' ')
                return num
        if c != num:
            num *= c
    return num
        
print(fatorial(6, show=True))