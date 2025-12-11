class Restaurante:
    def __init__(self, nome, categoria):
        lista_restaurantes = []
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        lista_restaurantes.append(self)

    
    def __str__(self):
        return f"""Nome Restaurante: {self.nome}\nCategoria: {self.categoria}\n Ativo: {self.ativo}"""



    def listar_restaurantes(cls):
        print(f'{'Nome Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Ativo'}')
        for restaurante_temp in cls.lista_restaurantes:
            print(f'{restaurante_temp.nome.ljust(25)} | {restaurante_temp.categoria.ljust(25)} | {restaurante_temp.ativo.ljust(25)}')


    @property
    def ativo(self):
        return '☑' if self._ativo else '☒'