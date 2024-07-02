import json
import requests
from deep_translator import GoogleTranslator

def traduzir_personagens():
    # URL da API que fornece os dados dos personagens
    api_url = 'https://last-airbender-api.fly.dev/api/v1/characters'
    
    # Fazendo a requisição GET para a API e obtendo a resposta
    response = requests.get(api_url)
    # imprime o retorno original
    print(json.dumps(response.json(), indent=4))
    
    # Convertendo a resposta da API para um objeto JSON
    personagens = response.json()
    
    # Instanciando o tradutor do deep-translator para traduzir do inglês para o português
    translator = GoogleTranslator(source='en', target='pt')
    
    # Lista para armazenar os personagens com atributos traduzidos
    personagens_traduzidos = []
    
    # Iterando sobre cada personagem na lista de personagens retornada pela API
    for personagem in personagens:
        # Traduzindo o nome do personagem para o português
        nome_traduzido = translator.translate(personagem['name'])
        
        # Traduzindo a afiliação do personagem para o português (ou definindo como "N/A" se não houver afiliação)
        afiliacao_traduzida = translator.translate(personagem.get('affiliation', 'N/A'))
        
        # Adicionando o personagem traduzido à lista de personagens traduzidos
        personagens_traduzidos.append({
            'nome': nome_traduzido,
            'afiliacao': afiliacao_traduzida
        })
    
    # Imprimindo a lista de personagens traduzidos em formato JSON com indentação e caracteres não-ASCII
    print(json.dumps(personagens_traduzidos, indent=4, ensure_ascii=False))

# Chamando a função para traduzir e exibir os personagens
traduzir_personagens()