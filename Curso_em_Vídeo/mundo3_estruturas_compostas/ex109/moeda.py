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
