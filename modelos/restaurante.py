from modelos.avaliacao import Avaliacao
#importando a classe avaliacao para ser utilizado dentro da classe restaurante.
class Restaurante:
    restaurantes = []
    # classe que representa um restaurante como inicio de nome, categoria e ativo ou não.
    def __init__(self, nome, categoria):
        self._nome = nome
        self._categoria = categoria
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
        # Aqui temos os atributos, nessa última linha temos um append que joga a instância na lista 
        # restaurantes utilizando o self dentro do append
        
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    # aqui é uma função principal que retorna um padrão sempre que a instancia for chamada, caso ela precise mostrar algo.    
        
    
        
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
    
    
    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    
    def alternar_estado(self):
        self._ativo = not self._ativo
        
        
    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)


    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliacao'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')