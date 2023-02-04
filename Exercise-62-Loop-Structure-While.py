# Exercicio resolvido por Cesar Augusto Numero 62 23/01/23
# Melhore o desafio 61, perguntando ao usuario se ele quer mostrar mais alguns termos. o programa encerra quando ele disser que quer mostrar 0 termos.

termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão do termo: '))
qnt_termo = int(input('Informe a quantidade de termos que deseja: '))
count = 0
termo_adicional = 0

while count != qnt_termo:
    # if qnt_termo != 0:
    print(termo, end=' ')
    termo += razao
    count += 1

    if count == qnt_termo:
        termo_adicional = int(
            input('\nQuantos termos você quer mostra a mais? '))
        qnt_termo += termo_adicional
print(f'Final mostrando {count} termos')
