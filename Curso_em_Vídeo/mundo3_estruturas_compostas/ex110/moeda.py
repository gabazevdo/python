def aumentar(valor=0, taxa=0, formato=False):
    res = valor + (valor * taxa / 100)
    
    if formato == True:
        return moeda(res)
    else:
        return res


def diminuir(valor=0, taxa=0, formato=False):
    res = valor - (valor * taxa / 100)

    if formato == True:
        return moeda(res)
    else:
        return res


def dobro(valor=0, formato=False):
    res = valor * 2

    if formato == True:
        return moeda(res)
    else:
        return res


def metade(valor=0, formato=False):
    res = valor / 2

    if formato == True:
        return moeda(res)
    else:
        return res


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')


def resumo(valor=0, taxaa=0, taxar=0):
    print(f'{taxaa}% de aumento: {aumentar(valor, taxaa, True)}')
    print(f'{taxar}% de redução: {diminuir(valor, taxar, True)}')
    print(f'Dobro: {dobro(valor, True)}')
    print(f'Metade: {metade(valor, True)}')
