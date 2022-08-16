cores = {
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'azul': '\033[34m',
    'amarelo': '\033[33m',
    'limpa': '\033[m',
}


def leiaInt(msg):

    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido...\033[m')
            continue
        else:
            return num


def linha(tam=40):
    print('-' * tam)


def cabecalho(txt):
    linha()
    print(txt.center(40))
    linha()


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    
    c = 1
    
    for item in lista:
        print(f'{cores["amarelo"]}{c}{cores["limpa"]} - {cores["azul"]}{item}{cores["limpa"]}')
        
        c += 1
    
    linha()

    opc = leiaInt('Sua opção: ')
    
    return opc
