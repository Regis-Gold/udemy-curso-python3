# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4
#  R e g i s
# -5-4-3-2-1
# para acessar o índice, usamos um número positivo ou negativo dentro de []

nome = 'Regis'
print(nome[2])
print(nome[-3])
print('g' in nome)
print('z' in nome)
print( 10 * '-')
print('g' not in nome)
print('z' not in nome)
print( 10 * '-')

nome2 = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome2:
    print(f'"{encontrar}": está em {nome2}')
else:
    print(f'"{encontrar}": não está em {nome2}')