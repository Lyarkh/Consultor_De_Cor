#pip install requests
import requests
from time import sleep

class ConsultorDeCor:
    def __init__(self, cor_em_hex):
        self.cor_em_hex = cor_em_hex
        print('Procurando cor...')
        sleep(1.5)
        print('Busca realizada!')
        self.__nome_cor = self.busca_nome_da_cor()
    
    @property
    def nome(self):
        return self.__nome_cor

    def __str__(self):
        return f'Nome da cor: {self.nome}' # Refatorar como será escrito, pois vai adicionar mais métodos

    def url_para_busca(self, tipo_de_pesquisa, formato='json'):
        return f'https://www.thecolorapi.com/{tipo_de_pesquisa}?hex={self.cor_em_hex}&format={formato}'

    def request_da_cor(self, tipo_de_pesquisa): # Request padrão que será utilizado na maioria  dos métodos
        url = self.url_para_busca(tipo_de_pesquisa)

        request_da_cor = requests.get(url)
        dados_da_cor = request_da_cor.json()
        return dados_da_cor

    def pega_nome_da_cor(self, banco_de_dados):
        nome_cor = banco_de_dados['name']['value']

        return nome_cor

    def schema_da_cor(self):
        dados_do_schema = self.request_da_cor('scheme')
        print(dados_do_schema)

    def pegando_todas_informacoes_da_cor(self):
        dados = self.request_da_cor('id')
      
        codigo_rgb = dados['rgb']['value']
        codigo_hsl = dados['hsl']['value']
        codigo_hsv = dados['hsv']['value'] 
        codigo_cmyk = dados['cmyk']['value']
        codigo_xyz = dados['XYZ']['value']
        imagem_da_cor = dados['image']['bare']
        contraste_da_cor = dados['contrast']['value']
        
        return codigo_rgb, codigo_hsl, codigo_hsv, codigo_cmyk, codigo_xyz, imagem_da_cor, contraste_da_cor
    
    def dicionario_dados(self):
        dicionario = self.pegando_todas_informacoes_da_cor()
        print(**dicionario)

if __name__ == "__main__":
    cor =  '00BFFF'
    nome_da_cor = ConsultorDeCor(cor)
    teste = nome_da_cor.dicionario()
    print(teste)
