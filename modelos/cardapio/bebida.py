from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho
        
    
    def __str__(self):
        return f'{self._nome} - {self._preco}'
    
    
    
    def descricaoCardapio(self):
        return 'bebida'
        
        
    def aplicar_desconto(self):
        porcentagem_desconto = 15
        self._preco -= (porcentagem_desconto / 100) * self._preco