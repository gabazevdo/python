# Vamos criar um menu, usando modularização.

from time import sleep
from lib.utils import *
from lib.arquivo import *

arq = 'arquivo.txt'

if arquivoExiste(arq):
    print('Arquivo encontrado!')
else:
    print('Arquivo não encontrado!')
    criaArquivo(arq)

while True:
    resp = menu(['Cadastrar nova pessoa', 'Ver pessoas cadastradas', 'Sair do sistema'])

    if resp == 1:
        cabecalho('NOVO CADASTRO')

        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')

        cadastrar(arq, nome, idade)
    elif resp == 2:
        lerArquivo(arq)
    elif resp == 3:
        cabecalho('Saindo do sistema...')
        break
    else:
        print(f'{cores["vermelho"]}ERRO! Digite uma opção válida...{cores["limpa"]}')
    
    sleep(1)
