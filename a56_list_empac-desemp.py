# Introdução ao desempacotamento

# desempacotamento é criar váriaveis com cada um dos valores da lista
nomes = ['Maria', 'Helena', 'Luiz']
nome1, nome2, nome3 = nomes
print(nome2)

# sempre que pegarmos um valor e a lista tiver uma quantidade maior do que estamos tentando desempacotar, pegamos o resto e passamos para uma variável.
nome4, *resto = ['Maria', 'Helena', 'Luiz']
print(nome4, resto)

# usamos underline *_ para informar que criamos a váriavel, mas não iremos usar
nome5, *_ = ['Maria', 'Helena', 'Luiz']
print(nome5)

# para pegarmos o segundo nome usamos underline _ para pular o primeiro valor
_, nome6, *_ = ['Maria', 'Helena', 'Luiz']
print(nome6)

