nome = "Regis Silva"
altura = 1.75
peso = 64
imc = peso / altura ** 2
print(nome, 'tem', altura, 'de altura')
print('pesa', peso, 'quilos e seu IMC é:')
print(imc)
print(...) # Pra não gerar erro no código enquanto você está digitando


print()
# f-strings > f'valor'
nome = "Regis Silva"
altura = 1.75
peso = 64
imc = peso / altura ** 2
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é:'
linha_3 = f'{imc:.2f}'
print(linha_1)
print(linha_2)
print(linha_3)
print(...) # Pra não gerar erro no código enquanto você está digitando