# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Métodos úteis:
# add, update, clear, discard

s1 = set()
s1.add('Reginaldo')
s1.add(98)
s1.update(('Boa tarde', 1, 2, 3, 4))
# s1.clear()
s1.discard('Boa tarde')
s1.discard('Reginaldo')
s1.add('Silva')
print(s1)