"""
dois underline são chamados de dander__
For + Range
range -> range(start, stop, step)

Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

texto = 'Regis' # iterável
iterador = iter(texto) # iterator

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break

print(10* '--->')

texto2 = 'Regis2' # iterável
iterador2 = iter(texto2) # iterator

for letra2 in texto2:
    print(letra2)