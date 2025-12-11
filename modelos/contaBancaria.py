class ContaBancaria:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo
        self._ativo = False

    
    def __str__(self):
        return f'Nome: {self.nome}, Saldo: R${self.saldo}.'
    

    @property
    def ativo(self):
        return '✔' if self._ativo else '✘'
    
    
    def alternar_status(self):
        self._ativo = not self._ativo


conta_1 = ContaBancaria('Mario', 57.5)
conta_2 = ContaBancaria('Sergio', 20000)

print(conta_1)
print()
print(conta_2)