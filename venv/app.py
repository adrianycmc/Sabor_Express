import requests
import json

url ='https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

#Get: verbo do HTTP que solicita uma requisição, pegar informações.
response = requests.get(url)
print(response)

#Função status_code: pega o status da requisição
if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        nome_do_restaurante = item ['Company']
        # Se o nome do restaurante não estiver em dados_restaurante é criado uma nova lista vazia
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []
            
        dados_restaurante[nome_do_restaurante].append({
            # Nesse dicionário, vamos definir a chave como item em minúsculo seguido de dois pontos
            "item": item['Item'],
            "price": item['price'],
            "description": item['description'] 
        })
      
else:
    print(f'O erro foi `{response.status_code}')

# Pegar o nome do restaurante e filtrar apenas os itens desses dados, pegar apenas os itens sem o nome do restaurante esplícito
for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    
    # Para conseguir criar esse arquivo, existe um comando Python que é with open, que permite manipular os arquivos também dentro da aplicação. A primeira informação é o arquivo e a segunda é o que quer fazer com esse arquivo, 'w' de write escrever no arquivo.
    with open(nome_do_arquivo,'w') as arquivo_restaurante:
        # Parâmetros do dump: 1º: quais são os dados que quero exibir; 2º: o nome do arquivo que estamos trabalhando; 3º: a identação
        json.dump(dados,arquivo_restaurante, indent=4)

    
print(dados_restaurante['McDonald’s'])
