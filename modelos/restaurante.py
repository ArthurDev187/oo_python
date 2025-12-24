from modelos.avaliacao import Avaliacao
"""Importando a classe Avaliacao."""


class Restaurante:
    restaurantes = []
    """Classe que representa um restaurante com uma lista que pertence a classe."""
    
    

    def __init__(self, nome, categoria):
        self._nome = nome
        self._categoria = categoria
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
        """Método que inicia a instância já com seus atributos e solicitando os argumentos principais.
        Uma atenção especial aqui para a adição que está acontecendo da instância dentro da lista que pertence a classe, 
        mantendo assim todas as instâncias dentro da lista chamada restaurantes."""
        

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    """Essa é uma função que retorna uma string sempre que a instância for chamada e precisar mostrar alguma coisa."""
        
    
    @property
    def nome(self):
        return self._nome
    """Esse é um getter do nome."""
    
    
    @nome.setter
    def nome(self, novo_nome):
        if novo_nome == None:
            print('Não foi digitado nenhum nome.')
            return
        self._nome = novo_nome
        print('Nome atualizado.')
        """Esse é uma setter do nome com uma validação antes de atualizar o nome, 
        para garantir que não seja inserido uma string vazia no lugar do nome do restaurante."""
        
    
    @property
    def categoria(self):
        return self._categoria
    """Esse é um getter da categoria"""
    
    @categoria.setter
    def categoria(self, nova_categoria):
        if nova_categoria == None:
            print('Não foi digitada nenhuma categoria.')
            return
        self._categoria = nova_categoria
        print('Categoria atualizada.')
        """Esse é um setter da categoria com a validação para que não seja aceito um campo vazio."""
    
    
    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    """Esse é um getter do atributo ativo, aqui ele retorna um ícone para se for verdadeiro e outra caso seja falso."""
    
    
    def alternar_estado(self):
        self._ativo = not self._ativo
        """Essa função é utilizada para alterar o estado do atributo ativo."""
        
        
    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
            """Essa função é para receber uma instância da avaliação, no caso cada cliente e sua avaliação."""


    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
    """Essa função faz o cálculo da média das avaliações."""
    
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliacao'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')
            """Essa função printa uma lista formatada com todos os restaurantes na lista restaurantes da classe."""