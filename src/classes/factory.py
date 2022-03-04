from .classes_para_factory.consultor_de_cor import ConsultorDeCor
from .classes_para_factory.tradutor import Tradutor

# Criando uma classes para criação de objetos de outras classes
class Fabrica:

    # Ele irá criar um objeto da classe ConsultorDeCor
    def cria_consultor_de_cor(self, cor):
        return ConsultorDeCor(cor)
    
    # Ele irá criar um objeto da classe Tradutor
    def cria_tradutor(self):
        return Tradutor()