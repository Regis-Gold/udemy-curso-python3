# Conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int, float, bool
print(int('1'), type(int('1'))) # 1 <class 'int'>
print(type(float('1') + 1)) # <class 'float'>
print(bool('')) # False
print(bool(' ')) # True
print(str(11) + 'dias') # 11dias