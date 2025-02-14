# Tipos int e float
# int -> Número inteiro
# O tipo int representa qualquer número
# positivo ou negativo. int sem sinal é considerado positivo.
print(10) # int literal
print(-10) # int literal
print(0) # int literal

# float -> Número com ponto fluturante
# O tipo float representa qualquer número
# positivo ou negativo com ponto flutante.
# float sem sinal é considerado positivo.
print(1.1, 10.11) # float
print(0.0, -1.5) # float

# A função type mostra o tipo que o Python inferiu ao valor.
print(type("Regis")) # <class 'str'>
print(type(-10)) # <class 'int'>
print(type(10.10), type(-10)) # <class 'float'> <class 'int'>