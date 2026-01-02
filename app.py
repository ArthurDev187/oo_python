from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato



restaurante_1 = Restaurante('Bays Water', 'Gourmet')
restaurante_2 = Restaurante('Japa nes', 'Comida japonesa')
restaurante_3 = Restaurante('Churras', 'Churrasco gourmet')
restaurante_4 = Restaurante('Piazza', 'Italiano')

prato_1 = Prato('Lasanha', 28.0, 'Lasanha a bolonhesa')
prato_2 = Prato('Pizza', 32, 'Supreme pizza')
bebida_1 = Bebida('Suco de laranja', 5.0, 'Grande')
bebida_2 = Bebida('Grarana antartica', 4.0, 'Media')





def main():
    print(f'Prato 1: {prato_1}')
    print(f'Prato 2: {prato_2}')
    print('=' * 45)
    print(f'Bebida 1: {bebida_1}')
    print(f'Bebida : {bebida_2}')
    print('Ola mundo')
    restaurante_1.incluir_item_cardapio(prato_1)
    restaurante_1.incluir_item_cardapio(bebida_1)

if __name__ == '__main__':
    main()
    
