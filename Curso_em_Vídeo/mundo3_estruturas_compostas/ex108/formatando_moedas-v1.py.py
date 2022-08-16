# Adapte o código do "ex107", criando uma função adicional chamada moeda() que consiga mostrar os números como um valor
# monetário formatado.

import moeda

print()

valor = float(input('Informe um valor: R$'))

print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(valor, 10))}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
print()
