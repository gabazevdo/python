# Dentro do pacote "utilidadescev" que criamos no "ex111", temos um módulo chamado dados.py. Crie uma função chamada
# leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas
# valores que sejam monetários.

from utilidadescev import moeda, dados

print()

valor = dados.leiaDinheiro('Informe um valor: R$')

moeda.resumo(valor, 10, 10)
print()
