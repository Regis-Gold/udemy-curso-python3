"""
Iterando strings com while
"""
#       123456789... Indíces 
nome = input('Digite seu nome: ') # Iteráveis

# nova_string += '*R*e*g*i*s* *S*i*l*v*a*'

i = 0
novo_nome = ''
while i < len(nome):
    letra = nome[i]
    novo_nome += f'*{letra}'
    i += 1
    
print(novo_nome)