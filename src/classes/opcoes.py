from .classes_mae.template_opcao import TemplateOpcao
from .classes_mae.voltar_menu import VoltarMenu

class Opcao01(TemplateOpcao, VoltarMenu):

    def run(self):
        print('esta funcionando a opção 01')
        self.volta_para_o_menu()

    def muda_estado(self):
        return 1

class Opcao02(TemplateOpcao,VoltarMenu):

    def run(self):
        print('esta funcionando a opção 02')
        self.volta_para_o_menu()
    
    def muda_estado(self):
        return 1

class Opcao03(TemplateOpcao,VoltarMenu):

    def run(self):
        print('esta funcionando a opção 03')
        self.volta_para_o_menu()
    
    def muda_estado(self):
        return 1

class Encerramento(TemplateOpcao):

    def run(self):
        print('esta funcionando a opção 07')
        input('pressione qualquer tecla para continuar')
    
    def muda_estado(self):
        #utilizado para mudar o estado do menu e encerrar o programa.
        print('-----------------------')
        print('Encerrando o programa!!')
        print(' ---até a próxima---!  ')

        return 0  
