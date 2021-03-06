#pip install requests
import requests

class Tradutor:
    def __init__(self, source='en', target='pt'):
        self.lingua_source = source
        self.lingua_target = target
        
    def __str__(self):
        return self.palavra_traduzida

    def traduzir(self, palavra_para_traducao):
        # testando API para tradução 
        url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

        key_da_api = self.__pega_chave_api()

        payload = f"q={palavra_para_traducao}&target={self.lingua_target}&source={self.lingua_source}"
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'accept-encoding': "application/gzip",
            'x-rapidapi-host': "google-translate1.p.rapidapi.com",
            'x-rapidapi-key': f"{key_da_api}" # Pegar a sua própia key na documentação da API
            }

        return self.__resposta(url, payload, headers)

    def __resposta(self, url, payload, headers):
        # fazendo busca com request e pegando os dados em json
        response = requests.request("POST", url, data=payload, headers=headers)
        response_json = response.json()

        nome_traduzido = response_json['data']['translations'][0]['translatedText']

        return  nome_traduzido
    
    def __pega_chave_api(self):
        with open('src/key_tradutor_API.txt', mode = 'r') as arquivo_chave:
            key_api = arquivo_chave.readline()
        
        return key_api

if __name__ == "__main__":
    texto = 'I love you'
    tradutor = Tradutor()
    traduzir = tradutor.traduzir(texto)
    
    print(traduzir)
