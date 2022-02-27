from .classes_para_factory.consultor_de_cor import ConsultorDeCor

class Fabrica:

    def cria_consultor_de_cor(self, cor):
        return ConsultorDeCor(cor)