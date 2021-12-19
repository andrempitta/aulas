
import requests
import tqdm


link = 'https://cep.awesomeapi.com.br/json/'


lista_ceps = [60165090, 60160200, '05642001']

for cep in lista_ceps:
    pesquisa = requests.get(f'https://cep.awesomeapi.com.br/json/{cep}')
    print(pesquisa)