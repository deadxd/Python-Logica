# Exercicio resolvido por Cesar Augusto Numero 114 31/01/23
# Crie um código em Python que teste se o site pudim.com.br está acessível pelo computador usado.

import urllib
import urllib.request

try:
    url = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Deu erro')
else:
    print('Tudo OK')
    print(url.read())
