# Crie um código que teste se o site "Pudim" está acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessível.')
else:
    print('O site Pudim está acessível.')
