"""
Caso tenha um while dentro do outro,  break e continue são usados no laço while mais próximo


"""

contador = 0

while contador <= 100:
    contador += 1

    if contador == 5:
        print(f'Não vou mostrar o {contador}')
        continue
    if contador >= 10 and contador <= 30:
        print(f'Não vou mostrar a linha {contador}')
        continue
    print(contador)

    if contador == 50:
        break