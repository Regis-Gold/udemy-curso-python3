# REVER ESSE CÓDIGO E ENTENDER A LÓGICA
# SE EU ENTENDER CERTINHO EU POSTO NA PAGE
""" Calculadora com while"""
while True:
    num_1 = input('Digite o 1° número: ')
    num_2 = input('Digite o 2° número: ')
    operador = input('Escolha um operador (+-/*): ')

    num_validos = None
    num_flt_1 = 0
    num_flt_2 = 0

    try:
        num_flt_1 = float(num_1)
        num_flt_2 = float(num_2)
        num_validos = True
    except:
        num_validos = None

    if num_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operador_permitido = '+-/*'

    if operador not in operador_permitido:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Confira o resultado abaixo:')
    if operador == '+':
        print(f'A soma de: {num_flt_1} + {num_flt_2} =', num_flt_1 + num_flt_2)
    elif operador == '-':
        print(f'A subtração de: {num_flt_1} - {num_flt_2} =', num_flt_1 - num_flt_2)
    elif operador == '/':
        print(f'A divisão de: {num_flt_1} / {num_flt_2} =', num_flt_1 / num_flt_2)
    elif operador == '*':
        print(f'A multiplição de: {num_flt_1} * {num_flt_2} =', num_flt_1 * num_flt_2)
    else:
        print('Nunca deveria chegar aqui.')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    print(sair)

    if sair is True:
        break