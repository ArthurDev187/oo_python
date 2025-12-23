from modelos.avaliacao import Avaliacao
#importando a classe avaliacao para ser utilizado dentro da classe restaurante.
class Restaurante:
    restaurantes = []
    # classe que representa um restaurante como inicio de nome, categoria e ativo ou não.
    def __init__(self, nome, categoria):
        self._nome = nome
        self._categoria = categoria
        self._ativo = False
        
        
    def __str__(self):
        return f'{self._nome} | {self._categoria}'    
        
    
    
    
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        if novo_nome == None:
            print('Não foi digitado nenhum nome.')
            return
        self._nome = novo_nome
        print('Nome atualizado.')
    
    @property
    def categoria(self):
        return self._categoria
    
    @categoria.setter
    def categoria(self, nova_categoria):
        if nova_categoria == None:
            print('Não foi digitada nenhuma categoria.')
            return
        self._categoria = nova_categoria
        print('Categoria atualizada.')
    
    