"""
split e join com list e str
split - divide uma string (list)
join - une uma string
strip - corta os espaços (rstrip e lstrip (esq/dir))

Podemos utilizar para fazer alterações em strings, nesse exemplo podemos ver a lista crua e tratada
"""

frase = "    Olha só que   ,    coisa interessante   "
lista_frases_cruas = frase.split(",")

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())
print(lista_frases_cruas)
print(lista_frases)

# Usando join para unir uma string, podemos usar apenas com iteraveis, se passarmos um número irá gerar um TypeError: can only join an iterable
print("\n-----------------------------------------")
frases_unidas = '-'.join(lista_frases)
print(frases_unidas)

print("\n-----------------------------------------")
frases_unidas2 = '-'.join("abcdefghijklmnopqrstuvwxyz")
print(frases_unidas2)