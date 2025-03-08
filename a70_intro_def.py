"""
Introdução às funções (def) em Python
Funções são trechos de código usados para replicar
determinada ação ao longo do código.
Elas podem receber valores para parâmetros
(argumentos) e retornar um valor específico.
Por padrão, funções Python retornam None (nada)
"""

# def Print():
#     print('Valor 1')
#     print('Valor 2')
#     print('Valor 3')
#     print('Valor 4')
# Print()

# def imprimir(a, b, c):
#     print(a, b, c)
# imprimir(1, 2, 3)
# imprimir(4, 5, 6)

def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')

saudacao('Reginaldo Silva')
saudacao('Afonso')
saudacao('Maria')
saudacao()
print(30 * '-')

def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é multiplo de {multiplo}?', end=' ')
    print(resultado)

multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)
