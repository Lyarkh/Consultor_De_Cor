#pip install requests
import requests
from time import sleep

class NomeDaCor:
    def __init__(self, cor_em_hex):
        self.cor_em_hex = cor_em_hex
        print('Criando objeto da cor...')
        sleep(1.5)
        self.nome_cor = self.busca_nome_da_cor_com_api(self.cor_em_hex)
    
    def __str__(self):
        return self.nome_cor

    def busca_nome_da_cor_com_api(self, cor_em_hexadecimal):
    # testando API para encontrar a cor com request

        url = f'https://www.thecolorapi.com/id?hex={cor_hexadecimal}'

        request_da_cor = requests.get(url)
        dados_da_cor = request_da_cor.json()

        nome_cor = dados_da_cor['name']['value']
        return nome_cor

class Tradutor:
    def __init__(self, palavra, target='pt', source='en'):
        self.palavra_sem_traducao = palavra
        self.lingua_source = source
        self.lingua_target = target
        self.palavra_traduzida = self.traduzir(self.palavra_sem_traducao)
        
    def __str__(self):
        return self.palavra_traduzida

    def traduzir(self, palavra_para_traducao):
        # testando API para tradução 
        url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

        payload = f"q={palavra_para_traducao}&target={self.lingua_target}&source={self.lingua_source}"
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'accept-encoding': "application/gzip",
            'x-rapidapi-host': "google-translate1.p.rapidapi.com",
            'x-rapidapi-key': "your key here" # Pegar a sua própia key na documentação da API
            }

        response = requests.request("POST", url, data=payload, headers=headers)
        response_json = response.json()

        nome_traduzido = response_json['data']['translations'][0]['translatedText']

        return  nome_traduzido

if __name__ == "__main__":
    cor_hexadecimal = '6495ED'
    nome_da_cor = NomeDaCor(cor_hexadecimal)
    tradutor = Tradutor(nome_da_cor)
    print(tradutor)
    
    