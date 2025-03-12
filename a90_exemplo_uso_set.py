# Exemplo de uso dos sets

letras = set()
while True:
    letra = input('Descubra a letra: ')
    letras.add(letra.lower())

    if 's' in letras:
        print('Você encontrou a letra correta "Fechando o programa 👋"')
        break

    print(letras)