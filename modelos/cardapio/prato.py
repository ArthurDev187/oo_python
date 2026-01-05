from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self.descricao = descricao
    
    def __str__(self):
        return f'{self._nome} - {self._preco}'
    
    def descricaoCardapio(self):
        return 'prato'
    
    def aplicar_desconto(self):
        porcentagem_desconto = 10
        self._preco -= (porcentagem_desconto / 100) * self._preco