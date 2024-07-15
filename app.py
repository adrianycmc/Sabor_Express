from modelos.restaurante import Restaurante
from modelos.avaliacao import Avaliacao
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida ('Suco de Cajú', 5.0, 'Grande')
prato_paozinho = Prato('Paozinho', 2.0, 'Pão doce especial da casa')

def main():
    print(bebida_suco)
    print(prato_paozinho)

if __name__ == '__main__':
    main()