class Livro:
    def __init__(self, titulo='', autor='', paginas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        
    def __str__(self):
        return f'{self.titulo} por {self.autor} - {self.paginas} paginas'
    
    @property
    def titulo_autor(self):
        return f'{self.titulo} por {self.autor}'
    
    def aumentar_paginas(self, quantidade):
        self.paginas += quantidade 
        
        
livro_1 = Livro('Lua cheia', 'Mayer may', 600)
print(livro_1)
print()
livro_1.aumentar_paginas(300)
print(livro_1)