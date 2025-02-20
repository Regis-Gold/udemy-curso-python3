"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
num_str = input('Vou dobrar seu número: ')

try:
    num_float = float(num_str)
    print(f'FLOAT: {num_float}')
    print(f'O dobro de {num_str} é {num_float * 2:.2f}')
except:
    print('Isso não é um número')