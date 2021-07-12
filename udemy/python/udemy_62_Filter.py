"""
Filter

filter() -> Serve para filtar dados de uma determinada coleção.

"""

valores = 1, 2, 3, 4, 5, 6
media = sum(valores) / len(valores)
print(media)

# Biblioteca para trabalhar com dados estatísticos
import statistics

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média usando a função mean()
média = statistics.mean(dados)
print(média)

# OBS: Assim como a função map(), a função filter() recebe dois valores, uma função e um iterável.
res = filter(lambda x: x > média, dados)
print(list(res))

# OBS: Assim como na função map(), após serem utiliazados os dados de filter(), eles são excluídos da memória.

# Outro exemplo:

paises = ['', 'Aregentina', '', 'Brasil', '', 'Chile', 'Equador', 'Colombia', '', '', 'Venezuela']
print(paises)
res = filter(None, paises)
print(list(res))
# OU
res1 = filter(lambda pais: len(pais) > 0, paises)
print(list(res1))
# OU
res2 = filter(lambda pais: pais != '', paises)
print(list(res2))