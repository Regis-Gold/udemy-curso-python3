"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
entrada = input('Digite seu "PRIMEIRO" nome: ')
nome = len(entrada)

if nome > 2:
    if nome <= 4:
        print('Seu nome é curto')
    elif nome >= 5 and nome <= 6:
        print('Seu nome é normal')
    elif nome  >= 6:
        print('Seu nome é muito grande')
    # else: int(nome)
    # print(f'"{nome}" não é um nome válido')
else:
    print(f'"Digite mais de "DUAS" letras')

