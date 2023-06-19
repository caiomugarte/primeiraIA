from jogador import Jogador
import random
class Ia(Jogador):
    def __init__(self, fichas):
        super().__init__(fichas)

    
    """
    Aqui a gente precisa 
    """
    def get_acao(self):
        return random.choice(self.acoes_possiveis)
    
    def get_raise(self, aposta_min=None):
        return random.choice(range((aposta_min*2),self.fichas))