import requests


UF= "12"
url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/{}/mesorregioes".format(UF)

response = requests.get(url).json()

print("Sigla: {}\n"
      "Nome: {}\n"
      "Região: {}".format(
      response[0]['UF']['sigla'],
      response[0]['UF']['nome'],
      response[0]['UF']['regiao']['nome']
      ))
