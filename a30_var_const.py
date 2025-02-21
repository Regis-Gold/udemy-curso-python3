"""
CONSTANTE = "Variáveis" que não vão mudar
CONTASTES sempre são representadas por letras maiúsculas
Muitas condições no mesmo if (ruim)
<- Contagem de complexidade (ruim) identação distante
"""
velocidade = 51 # velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 60 # Velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distáncia onde o radar pega

loc_menos_range = LOCAL_1 - RADAR_RANGE # 99
loc_mais_range = LOCAL_1 + RADAR_RANGE # 101

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_multado_radar_1 = (local_carro >= \
loc_menos_range) and (local_carro <= loc_mais_range)
carro_multado_sim_nao = carro_multado_radar_1 and \
    vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('O carro está acima da velocidade')
else:
    print('O carro "NÃO" está acima da velocidade')

if  carro_multado_sim_nao:
    print('O carro foi multado no RADAR_1')
else:
    print('O carro "NÃO" foi multado no RADAR_1')

