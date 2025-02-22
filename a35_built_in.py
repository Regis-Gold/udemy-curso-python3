"""
# https://docs.python.org/3/library/stdtypes.html

built in: é o tipo que já vem no Python(não precisamos instalar)

Imutáveis que vimos: str, int, float, bool
Não tem como mudar o valor, teriamos que criar outra variavel 

str, intm float, bool são objetos, e existe ações que podemos executar dentro deses objetos
"""

string = 'Regis Silva'
outra_variavel = string
# string[5] = '123' # isso gera um erro
# fariamos essa mudança dessa forma:
outra_variavel = f'{string[:5]}123{string[6:]}'
print(string)
print(outra_variavel)
print(string.zfill( 20)) # qtde de 0 a esquerda