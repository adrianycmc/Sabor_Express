from modelos.restaurante import Restaurante
from modelos.avaliacao import Avaliacao

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('El Mexiano', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

restaurante_mexicano.alternar_estado()

restaurante_praca.receber_avaliacao('Adriany', 4)
restaurante_praca.receber_avaliacao('Mayara', 6.7)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()