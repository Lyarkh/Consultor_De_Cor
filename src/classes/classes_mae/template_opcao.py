from abc import ABCMeta, abstractmethod

class TemplateOpcao(metaclass=ABCMeta):

    @abstractmethod
    def run(self):
        pass
    
    @abstractmethod
    def muda_estado(self):
        pass
    