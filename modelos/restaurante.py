from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio


class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        # A função title() do Python deixa a primeira letra da palavra maiúscula, upper() função que deixa todas as letras maiúsculas.
        # Atributo privado tem o underline, para acessar também precisa do underline.
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    # Self: referência atual da instância que está chamando
    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    # @classmethod indica que se trata de um método da classe, o cls é convencionamente usado como argumento.
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')
                      

    def alternar_estado(self):
        self._ativo = not self._ativo

    # @property modifica como o atributo é lido
    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5: 
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    # É um @property porque é um médodo capaz de ser lido
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        # A função round arredonda os cálculos o (,1) é a quantidade de vídeos que vai querer.
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
        
    def adicionar_no_cardapio(self, item):
        
        #instance verifica se está dentro da classe. É verdadeira se o item que passou como argumento for uma instancia da classe derivada. 
        if isinstance (item, ItemCardapio):
            self._cardapio.append(item)

    @property            
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}\n')
        for i,item in enumerate(self._cardapio,start=1):
           if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
           else: 
               mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}'
               print(mensagem_bebida)
            