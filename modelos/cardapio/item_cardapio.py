from abc import ABC, abstractmethod


class ItemCardapio:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
        

    @abstractmethod
    def descricaoCardapio(self):
        pass 

    
    @abstractmethod
    def aplicar_desconto(self):
        pass
    
    