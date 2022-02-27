from classes.factory import Fabrica
from classes.menu import Menu

class Principal:

    def teste_da_cor(self):
        cor =  '00BFFF'
        nome_da_cor = Fabrica().cria_consultor_de_cor(cor)
        print(nome_da_cor.nome)
        print(nome_da_cor)

    def main(self):
        menu = Menu().run()


if __name__ == "__main__":
    main = Principal().teste_da_cor()
    