from modelos.restaurante import Restaurante
from modelos.avaliacao import Avaliacao
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida ('Suco de Cajú', 5.0, 'Grande')
prato_paozinho = Prato('Paozinho', 2.0, 'Pão doce especial da casa')

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

bebida_suco.aplicar_desconto()
prato_paozinho.aplicar_desconto()

def main():
    restaurante_praca.exibir_cardapio
    


if __name__ == '__main__':
    main()