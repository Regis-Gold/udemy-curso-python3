# parâmetro nomeado, é quando damos o nome para a chamadas das funções, ou da criação das funções
# quando a função está dentro de um objeto, ela é chamada de método
a = 'AAA'
b = 'BBB'
c = 1.1
string1 = 'a={} b={} c={}'
formato = string1.format(a, b, c)
print(formato)
print()

a = 'AAA'
b = 'BBB'
c = 1.1
string1 = 'c={nome3} a={nome1} b={nome2}'
formato = string1.format(nome1=a, nome2=b, nome3=c)
print(formato)