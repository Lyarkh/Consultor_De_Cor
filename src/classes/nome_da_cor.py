#pip install requests
import requests
from time import sleep

class NomeDaCor:
    def __init__(self, cor_em_hex):
        self.cor_em_hex = cor_em_hex
        print('Procurando o nome da cor...')
        sleep(1.5)
        self.__nome_cor = self.busca_nome_da_cor_com_api(self.cor_em_hex)
    
    @property
    def nome(self):
        return self.__nome_cor

    def __str__(self):
        return f'Nome da cor: {self.nome}'

    def busca_nome_da_cor_com_api(self, cor_em_hexadecimal):
    # testando API para encontrar a cor com request

        url = f'https://www.thecolorapi.com/id?hex={cor_em_hexadecimal}'

        request_da_cor = requests.get(url)
        dados_da_cor = request_da_cor.json()

        nome_cor = dados_da_cor  # ['name']['value'] 
        return nome_cor