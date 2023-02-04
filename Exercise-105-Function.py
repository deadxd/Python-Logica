#Exercicio resolvido por Cesar Augusto Numero 105 30/01/23
    #Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
        #A) Quantidade de notas
        #B) A maior nota
        #C) A menor nota
        #D) A média da turma
        #E) A situação (opcional)
            #Adicione também docstrings para a função

def notas(*notas, sit=0):
    count = 0
    notas_dict = {}
    maior = menor = 0
    soma = 0
    for each in notas:
        if count == 0:
            maior = each
            menor = each
        elif each > maior:
            maior = each
        elif each < menor:
            menor = each
        count +=1
        soma += each
    media = soma / count
    notas_dict['total'] = count
    notas_dict['maior'] = maior
    notas_dict['menor'] = menor
    notas_dict['media'] = f'{media :0.1f}'
    if sit != 0:
        if media >= 7:
            notas_dict['situação'] = 'BOA'
        elif media > 5:
            notas_dict['situação'] = 'RAZOÁVEL'
        else: 
            notas_dict['situação'] = 'RUIM'
    return notas_dict 
    '''
    -> Calculo de notas dos alunos
    :param notas: recebendo varias notas
    '''
    
resp = notas(6.5,5.5,7.6,8.8,8, sit=True)
print(resp)