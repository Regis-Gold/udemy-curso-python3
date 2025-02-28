"""
Exercício
exiba os indices da lista
0 Maria
1 Helena
2 Luiz
for in com listas
como a lista é um iteravel podemos usar for
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))