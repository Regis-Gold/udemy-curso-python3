"""
Flag (Bandeira) - Marcar um local
Nome = Não valor
is e is not = é ou não é (tipo, valor, id)
id = Identidade
"""

v1 = 'a'
v2 = 'a'
print(id(v1))
print(id(v2))
print(5 * "¬¬¬¬¬")

condicao = False
passou_if = None

if condicao:
    passou_if = True
    print('Faça algo')
else:
    print('Não faça algo')

if passou_if is None:
    print('Não passou no if')
else:
    print('Passou no if')
