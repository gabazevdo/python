# Modifique as funções que foram criadas no "ex107" para que elas aceitem um parâmetro a mais, informando se o valor
# retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no "ex108".

import moeda

print()

valor = float(input('Informe um valor: R$'))

print(f'Aumentando 10%, temos {moeda.aumentar(valor, 10, True)}')
print(f'Diminuindo 10%, temos {moeda.diminuir(valor, 10, True)}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, True)}')
print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}')
print()
