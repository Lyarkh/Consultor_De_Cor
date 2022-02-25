import os
from time import sleep

class Carregamento:

    @staticmethod
    def com_ponto():
        os.system('cls')
        
        print('Carregando', end='')

        ponto = '.'
        for _ in range(4):
            print(ponto, end='')
            sleep(0.2)
        
        os.system('cls')
        