"""
Delta de Data e Hora

data_inicial = 15/05/1975 12:55:32.233445
data_final = 15/05/2021 10:25:12.223566
delta = data_final - data_inicial

"""
import datetime

# Data de hoje
data_hoje = datetime.datetime.now()

# Data para ocorrer um determinado evento
aniversario = datetime.datetime(2021, 5, 15)

tempo_para_evento = aniversario - data_hoje

print(type(tempo_para_evento))
print(repr(tempo_para_evento))
print(tempo_para_evento)

print(f'Faltam {tempo_para_evento.days} dias e {tempo_para_evento.seconds // 60 // 60} horas.')


# ----------------------------------------------------------------------------------------------
print(f'-_'*30, end='\n\n')

data_compra = datetime.datetime.now()
print(data_compra)
regra_boleto = datetime.timedelta(days=3)
print(regra_boleto)

data_pgto_boleto = data_compra + regra_boleto
print(data_pgto_boleto)


# ----------------------------------------------------------------------------------------------
print(f'-_'*30, end='\n\n')
