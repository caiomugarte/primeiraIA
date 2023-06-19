class Jogador:
    def __init__(self, fichas) :
        self.cartas = []
        self.fichas = fichas
        self.posicao = ""
        self.acoes_possiveis = []
        self.ultima_acao = ""

    def get_acao(self):
        print('Jogador deve selecionar uma ação')

    def get_raise(self):
        print('Jogador deve selecionar a quantidade de fichas para Raise')