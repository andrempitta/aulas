
import requests
from tqdm import tqdm
from time import sleep

link = 'https://cep.awesomeapi.com.br/json/'


lista_ceps = ['60165090', '05642001', '60160200', 60123123 ,'05641001']


resutaldo = []
for cep in tqdm(lista_ceps):
    pesquisa = requests.get(f'https://cep.awesomeapi.com.br/json/{cep}')
    resutaldo.append(pesquisa.json())

print(resutaldo)



with tqdm(total=100) as barra_progresso:
    barra_progresso.update(10)
    sleep(2)
    barra_progresso.update(10)
    sleep(2)
    barra_progresso.update(10)
    sleep(2)
    barra_progresso.update(20)
    sleep(2)
    barra_progresso.update(50)
    sleep(2)
