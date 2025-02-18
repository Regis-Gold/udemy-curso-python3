# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

senha = input('Senha: ')

if not senha:
    print('Você não digitou nada.')

elif senha != '123':
    print('Senha incorreta.')

elif senha == '123':
    print('Conectado\n'
        'Carregando seus dados...')

print()
print('1', not True)
print('2', not False)
print('3', not 1)
print('4', not 0)