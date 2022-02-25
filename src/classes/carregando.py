from time import sleep

class Carregamento:

    @staticmethod
    def com_ponto():
        print('Carregando', end='')

        ponto = '.'
        for _ in range(4):
            print(ponto, end='')
            sleep(0.2)
            