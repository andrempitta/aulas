# MINHA SOLUÇãO
print('{:=^40}'.format(' TUPLAS '))
print(30*'=')
print('{:^30}'.format('TIMES CAMPEONATO BRASILEIRO'))
print(30*'=')

times = ('Internacional', 'Flamengo', 'São Paulo', 'Atlético-MG', 'Fluminense',
        'Palmeiras', 'Grêmio', 'Santos', 'Athletico-PR', 'Ceará', 'Corinthians',
        'Bragantino', 'Atlético-GO', 'Sport', 'Bahia', 'Fortaleza', 'Vasco',
        'Goiás', 'Coritiba', 'Botafogo')
print('✿' * 20)
print('Lista dos 20 Times do campeonato brasileiro:')
for t in times:
    print(t)
print('✿' * 20)
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print('✿' * 20)
print(f'Os 5 últimos colocados são {times[-4:]}')
print('✿' * 20)
print(f'Lista dos 20 times no Brasileirão hoje 21/02/2021 em ordem alfabética é: {sorted(times)}')


# Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
# do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.