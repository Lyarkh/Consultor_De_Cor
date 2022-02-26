from .classes_mae.template_opcao import TemplateOpcao
from .classes_mae.voltar_menu import VoltarMenu
from .carregando import Carregamento

class Opcao01(TemplateOpcao, VoltarMenu): # Buscar cor por codigo rgb ou hexadecimal

    def run(self):
        print('esta funcionando a opção 01')
        self.volta_para_o_menu()
        Carregamento.com_ponto()

    def muda_estado(self):
        return 1

class Opcao02(TemplateOpcao,VoltarMenu): # Todas as informações referentes a cor

    def run(self):
        print('esta funcionando a opção 02')
        self.volta_para_o_menu()
        Carregamento.com_ponto()
    
    def muda_estado(self):
        return 1

class Opcao03(TemplateOpcao,VoltarMenu): # Schema da cor

    def run(self):
        print('esta funcionando a opção 03')
        self.volta_para_o_menu()
        Carregamento.com_ponto()
    
    def muda_estado(self):
        return 1

class Encerramento(TemplateOpcao): # Sair do programa

    def run(self):
        print('esta funcionando a opção 07')
        Carregamento.com_ponto()
    
    def muda_estado(self):
        #utilizado para mudar o estado do menu e encerrar o programa.
        print('\n-----------------------')
        print('Encerrando o programa!!  ')
        print(' ---até a próxima---!    ')

        return 0  
