# Exercicio resolvido por Cesar Augusto Numero 113 31/01/23
# Reescreva a função leiaINT() que fizemos no exercicio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade


def leiaInt(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: Digite um INTEIRO valido')
            continue
        except KeyboardInterrupt:
            print('Usuario preferiu não digita esse campo de dados')
            return 0
        else:
            return inteiro


def leiaFloat(msg):
    while True:
        try:
            real = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: Digite um número REAL valido')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuario')
            return 0
        else:
            return real


inteiro = leiaInt('Digite um valor inteiro: ')
real = leiaFloat('Digite um valor real: ')
print(f'O número inteiro foi: {inteiro} e o número real foi: {real}')
