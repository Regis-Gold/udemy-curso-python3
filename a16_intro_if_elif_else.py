# if / elif      / else
# se / se não se / se não
entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('log in...')
    print('Você entrou no sistema')
    print(1010101010)
elif entrada == 'sair':
    print('log out...')
    print('Você saiu do sistema')
    print('Thanks! Bye Bye')
else:
    print('Você não digitou uma das opções')

print('FORA DOS BLOCOS')