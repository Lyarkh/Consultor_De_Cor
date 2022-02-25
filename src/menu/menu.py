import os
from time import sleep

from classes.template_opcao import TemplateOpcao

class Menu:
    def __init__(self):
        self.estado = 1 

    def run(self):
        self.apresenta_programa()
        sleep(0.8)
        
        while self.estado:
            self.limpa_tela()
            self.imprime_menu()
            self.escolha_opcao()

    def verificando_estado(self, estado)-> bool:
        self.estado = estado.muda_estado()
    
        return self.estado

    def apresenta_programa(self):
        print('Iniciando...')
        sleep(0.8)
        self.limpa_tela()
        print('│-------------------------------------------│') 
        print('│-----------------Bem vindo!!---------------│')
        print('│-------------------------------------------│')  

    def imprime_menu(self):
        print('│-------------------------------------------│')
        print('│-------------------Menu!!------------------│')
        print('│-------------------------------------------│')
        print('│(1)    Converter RGB para Hexadecimal      │')
        print('│(2)    Descobrir o nome da cor             │')
        print('│(3)    Traduzir cor ou outra palavra       │')
        print('│(4)    Informações do programa             │')
        print('│(5)    Opção 05                            │')
        print('│(6)    Opção 06                            │')
        print('│(7)    Sair do programa                    │')
        print('│-------------------------------------------│')
    
    def limpa_tela(self):
        os.system('cls')

    def escolha_opcao(self):
        lista_opcoes = [Opcao01(), Opcao02(), Opcao03(),
                        Opcao04(), Opcao05(), Opcao06(), Encerramento()]

        print('Qual opção deseja?')
        opcao_inserida = input('-> ').strip()
        opcao_tratada = self.tratamento_opcao(opcao_inserida)

        
        for id, _ in enumerate(lista_opcoes):
            if opcao_tratada == id+1:
                lista_opcoes[id].run()
                self.estado = self.verificando_estado(lista_opcoes[id])
    
    def tratamento_opcao(self, opcao):
        opcoes_aceitas = ['1','2','3','4','5','6','7']

        if opcao in opcoes_aceitas:
            return int(opcao)
        else:
            self.opcao_invalida()

    def opcao_invalida(self):
        print('│-------------------------------------------│')
        print('│         Digite uma opção válida           │')
        print('│       São aceitas opções de 1 a 7         │')
        print('│-------------------------------------------│')
        input('│Pressione qualquer tecla pra voltar ao menu│')   
            
        print('Carregando', end='')

        for _ in range(4):
            ponto = '.'
            print(ponto, end='')
            sleep(0.5)

class Opcao01(TemplateOpcao):

    def __str__(self):
        return 'opcao_1'
    
    def run(self):
        print('esta funcionando a opção 01')
        input('pressione qualquer tecla para voltar para o menu')

    def muda_estado(self):
        return 1

class Opcao02(TemplateOpcao):

    def __str__(self):
        return 'opcao_2'
    
    def run(self):
        print('esta funcionando a opção 02')
        input('pressione qualquer tecla para voltar para o menu')
    
    def muda_estado(self):
        return 1

class Opcao03(TemplateOpcao):

    def __str__(self):
        return 'opcao_3'
    
    def run(self):
        print('esta funcionando a opção 03')
        input('pressione qualquer tecla para voltar para o menu')
    
    def muda_estado(self):
        return 1

class Opcao04(TemplateOpcao):

    def __str__(self):
        return 'opcao_4'
    
    def run(self):
        print('esta funcionando a opção 04')
        input('pressione qualquer tecla para voltar para o menu')
    
    def muda_estado(self):
        return 1

class Opcao05(TemplateOpcao):

    def __str__(self):
        return 'opcao_5'
    
    def run(self):
        print('esta funcionando a opção 05')
        input('pressione qualquer tecla para voltar para o menu')
    
    def muda_estado(self):
        return 1

class Opcao06(TemplateOpcao):

    def __str__(self):
        return 'opcao_6'
    
    def run(self):
        print('esta funcionando a opção 06')
        input('pressione qualquer tecla para voltar para o menu')
    
    def muda_estado(self):
        return 1

class Encerramento(TemplateOpcao):

    def __str__(self):
        return 'opcao 07 - opcao_de_encerramento'
    
    def run(self):
        print('esta funcionando a opção 07')
        input('pressione qualquer tecla para continuar')
    
    def muda_estado(self):
        #utilizado para mudar o estado do menu e encerrar o programa.
        print('-----------------------')
        print('Encerrando o programa!!')
        print(' ---até a próxima---!  ')

        return 0

            

if __name__ == '__main__':
    menu = Menu().run()