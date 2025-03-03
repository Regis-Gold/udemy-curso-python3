"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html

O erro de imprecisão pode ser tradado das seguintes formas:
- Formatar o valor direto na saída como uma string
print(f"{numero_3:.2f}")

- Usando a função round dessa forma
print(round(numero_3, 2))

- Também podemos usar o modulo decimal, importamos o decimal, e convertemos os valores flutuantes para string assim teremos o valor original formatado


"""
import decimal

numero_1 = decimal.Decimal("0.1")
numero_2 = decimal.Decimal("0.7")
numero_3 = numero_1 + numero_2
print(numero_3)
print(f"{numero_3:.2f}")
print(round(numero_3, 2))
