from jogador import Jogador
import random
class RandomPlayer(Jogador):
    def __init__(self, fichas):
        super().__init__(fichas);

    def get_acao(self):
        acao = random.choice(self.acoes_possiveis)
        self.ultima_acao = acao
        return acao
    
    def get_raise(self, apostaMin):
        return random.choice(range((apostaMin*2),self.fichas))
