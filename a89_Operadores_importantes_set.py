# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2 # união
print(s3)

s3 = s1 & s2 # intersecção
print(s3)

s3 = s1 - s2 # diferença
print(s3)

s3 = s1 ^ s2 # diferença simétrica
print(s3)
