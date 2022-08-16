# Reescreva a função leiaInt() que fizemos no ex104, incluindo agora a possibilidade da digitação de um número de
# tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.


def leiaInt(msg):

    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido...\033[m')
            continue
        else:
            return num


def leiaFloat(msg):

    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número real válido...\033[m')
            continue
        else:
            return num


print()

num1 = leiaInt('Digite um número inteiro: ')
num2 = leiaFloat('Digite um número real: ')
print(f'Você digitou o número inteiro {num1} e o número real {num2}')

print()
