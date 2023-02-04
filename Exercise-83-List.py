# Exercicio resolvido por Cesar Augusto Numero 83 25/01/23
# Crie um programa onde o usuário digite uma expressão qualquer que use parenteses ().
# Seu aplicativo deverá analisar se a expressão passada está com os parenteses abertos e fechados na ordem correta.

expressao = str(input('Informe uma expressão matematica: ')
                ).strip()  # ((5+3)*6)

if expressao.count('(') == expressao.count(')'):
    print(f'A expressão: {expressao} esta correta!')
else:
    print(f'A expressão: {expressao} esta invalida faltando parenteses!')
