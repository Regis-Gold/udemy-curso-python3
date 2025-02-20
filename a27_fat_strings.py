"""
Fatiamento de strings
012345678
Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Regis Silva'
print('1-', variavel[2])
print('2-', variavel[-2])
print('3-', variavel[2:])
print('4-', variavel[:2])
print('5-', variavel[2:6])
print('6-', variavel[-6:-2])
print('7-', len(variavel))
print('6-', variavel[0:11:1])
print('6-', variavel[0:11:2])
print('6-', variavel[::-1])
print('6-', variavel[::-2])