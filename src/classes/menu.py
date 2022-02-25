import os
from time import sleep

from .carregando import Carregamento
from .opcoes import *

class Menu:
    def __init__(self):
        self.estado = 1 

    @property
    def lista_das_opcoes_disponiveis(self):
        lista_das_opcoes = [Opcao01(), Opcao02(), Opcao03(), Encerramento()]

        return lista_das_opcoes
        
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
        print('│------------------------------------------------│')
        print('│----------------------Menu!!--------------------│')
        print('│------------------------------------------------│')
        print('│(1)  Buscar cor por codigo rgb ou hexadecimal   │')
        print('│(2)  Todas as informações referentes a cor      │')
        print('│(3)  Schema da cor                              │')
        print('│(4)  Sair do programa                           │')
        print('│------------------------------------------------│')
    
    def limpa_tela(self):
        os.system('cls')

    def escolha_opcao(self):
        lista_opcoes = self.lista_das_opcoes_disponiveis

        print('Qual opção deseja?')
        opcao_inserida = input('-> ').strip()
        opcao_tratada = self.tratamento_opcao(opcao_inserida)

        for id, _ in enumerate(lista_opcoes):
            if opcao_tratada == id+1:
                lista_opcoes[id].run()
                self.estado = self.verificando_estado(lista_opcoes[id])
    
    def tratamento_opcao(self, opcao):
        lista_de_opcoes = self.lista_das_opcoes_disponiveis
        opcoes_aceitas = [str(posicao+1) for posicao in range(len(lista_de_opcoes))] 

        if opcao in opcoes_aceitas:
            return int(opcao)
        else:
            self.opcao_invalida()

    def opcao_invalida(self):
        self.limpa_tela()
        print('│-------------------------------------------│   ')
        print('│         Digite uma opção válida           │   ')
        print('│       São aceitas opções de 1 a 4         │   ')
        print('│-------------------------------------------│   ')
        input('│Pressione qualquer tecla pra voltar ao menu│\n ')   

        Carregamento.com_ponto()

"""
 Caso venha rodar o menu como arquivo principal,e occorer o erro:
 "ImportError: attempted relative import with no known parent package",
 mude como estão as importações de arquivo, basicamente tirando o "." antes de "classes" no import 
"""
if __name__ == '__main__':
    menu = Menu().run()
