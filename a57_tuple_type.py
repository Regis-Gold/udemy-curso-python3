"""
- Tipo tupla - uma lista imutável
- podemos usar todos os métodos de list
- a tupla é mais eficiente do que a lista
- quando não precisamos alterar a list podemos usar uma tuple

"""

# para criar uma tuple, tiramos os colchetes que teriam em uma list
nomes= 'Maria', 'Helena', 'Luiz' # tuple
# nomes[1] = 'Regis' gera um erro pois não podemos alterar o valor que é imutável

# para ser mais especificos podemos usar ()
nomes= ('Maria', 'Helena', 'Luiz') # tuple
print(nomes, type(nomes))
print(nomes[-1])
print(10*'- --')

# também podemos fazer a coerção de uma list para uma tuple
nomes= ['Maria', 'Helena', 'Luiz'] # list
nomes = tuple(nomes)
print(nomes, type(nomes))
print(nomes[-2])
print(10*'- --')

# ou de uma tuple para uma list
nomes = list(nomes)
print(nomes, type(nomes))
print(nomes[-3])


