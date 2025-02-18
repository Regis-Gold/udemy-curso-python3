# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira, avalia toda a expressão como verdadeira. 
# Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrando no sistema')
else:
    print('Saindo')

# Avaliação de curto circuito
senha = 0 or False or 0 or 'abc' or True
print(senha)

senha2 = input('Senha: ') or '"Insira uma senha válida"'
print(senha2)