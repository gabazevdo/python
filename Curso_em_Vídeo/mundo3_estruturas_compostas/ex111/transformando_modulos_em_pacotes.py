# Crie um pacote chamado "utilidadescev" que tenha dois módulos internos chamados moeda.py e dados.py. Transfira
# todas as funções utilizadas nos "ex107", "ex108" e "ex109" para o primeiro pacote e mantenha tudo funcionando.

from utilidadescev import moeda

print()

valor = float(input('Informe um valor: R$'))

moeda.resumo(valor, 10, 10)
print()
