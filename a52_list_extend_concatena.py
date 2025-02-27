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
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
print(lista_a) # lista a
print(lista_b) # lista b
print(lista_c) # união de a e b
lista_d = lista_a.extend(lista_b) # executa o metodo mas não nos mostra o valor
print(10*'- --')
print(lista_d) # extende o val. de _a para _b
print(lista_a) # aqui teremos a concatenação
