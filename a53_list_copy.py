"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
# = - copiado o valor (imutáveis)
# esses dois valores tem IDs diferentes
nome = 'Regis'
outra_var = nome
nome = 'Silva'
print(nome)
print(outra_var)
print(10*'- --')

# = - aponta para o mesmo valor na memória
lista_a = ['Regis', 'Silva', 1, True, 1.2]
lista_b = lista_a # apontam para o mesmo ID
lista_c = lista_a.copy() # copiamos o valor a
lista_a[0] = 'Outro nome' # reatribui a e b

print(lista_a)
print(lista_c)