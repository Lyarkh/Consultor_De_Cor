from abc import ABCMeta, abstractmethod

class TemplateOpcao(metaclass=ABCMeta):
    
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def run(self):
        pass
    
    @abstractmethod
    def muda_estado(self):
        pass