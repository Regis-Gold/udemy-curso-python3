"""
https://acervolima.com/python-string-interpolation/
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Regis'
preco = 1000.12343
variavel1 = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel1)
print('O hexadecimal de %d é %04x' % (25, 25))