"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
varialvel = 'CDEFGAB'
print(f'{varialvel}')
print(f'{varialvel:*>10}')
print(f'{varialvel:*<10}')
print(f'{varialvel:*^10}')
print(f'{1000.4124412:0=10,.2f}')
print(f'O hexadecimal de 25 é {25:04x}')
print(f'{varialvel!r}') # flag __repr__
print(f'{varialvel!s}') # flag __str__
print(f'{varialvel!a}') # flag __

