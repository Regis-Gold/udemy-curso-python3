"""
Exercício
exiba os indices da lista
0 Maria
1 Helena
2 Luiz
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

lista_enumerada = list(enumerate(lista))
print(lista_enumerada)
print(10*'- --')

for indice, nome in enumerate(lista):
    print(indice, nome)
print(10*'- --')

for item in enumerate(lista):
    print(item)

