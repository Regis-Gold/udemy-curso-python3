"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#         0   1   2   3   4   5
lista = [10, 20, 30, 40, 50, 60]
lista[2] = 300
del lista[2] # apaga itens da lista
print(lista)
print(lista[2])
print(10*'- --')

#         0   1   2   3   4   5
lista2 = [10, 20, 30]
lista2.append(50) # adc itens no fim da lista
print(lista2)
lista2.append(60) # adc itens no fim da lista
print(lista2)
lista2.append(70) # adc itens no fim da lista
print(lista2)
ultimo_item = lista2.pop() # remove o último item da lista
print(lista2)
print('Removido: ', ultimo_item)
lista2.pop(3) # removeu o índice 3
print(lista2)
print(10*'- --')

