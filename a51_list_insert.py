"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#         0   1   2   3   4   5
lista = [10, 20, 30, 40, 50, 60]
lista.append('Regis') # adiciona ao fim
lista.append('Silva')
sobrenome = lista.pop() # remove do fim
print(lista) # retorna a lista
print(sobrenome) # retorna a var com el pop
del lista[-1]
print(lista)
# lista.clear() # para limpar a lista
lista.insert(0, 5) # inserir o item no indice
print(lista)
