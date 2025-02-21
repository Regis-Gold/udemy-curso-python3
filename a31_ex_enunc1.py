"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# PRIMEIRA FORMA DE RESOLVER:
entrada = input('Digite um número interiro: ')

if entrada.isdigit():
    num_int = int(entrada)
    num_par = num_int % 2 == 0
    par_impar_texto = '"IMPAR"'

    if num_par:
        par_impar_texto = '"PAR"'

    print(f'O número {num_int} é inteiro e {par_impar_texto}')
else:
    print('Você "NÃO" digitou um número inteiro')


# SEGUNDA FORMA DE RESOLVER:
entrada = input('Digite um número interiro: ')

try:
    num_int = int(entrada)
    num_par = num_int % 2 == 0
    par_impar_texto = '"IMPAR"'

    if num_par:
        par_impar_texto = '"PAR"'

    print(f'O número {num_int} é inteiro e {par_impar_texto}')
except:
    print('Você "NÃO" digitou um número inteiro')
