# Precedência dos operadores

# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -
conta_1 = 1 + 1 ** 5 + 5 # 1 ** 5 = 1 + 5 + 1 = 7
conta_2 = (1 + 1) ** (5 + 5) # 2 ** 10 = 1024
conta_3 = (1 + int(0.5 + 0.5)) ** (5 + 5) # 1 + 1 ** 10 = 1024
print(conta_1)
print(conta_2)
print(conta_3)

conta_1 = 'Um outro valor' # alterou o valor da váriavel conta_1
print(conta_1) 
