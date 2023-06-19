from baralho import Baralho
from mesa import Mesa
from randomPlayer import RandomPlayer
from ia import Ia
from dealer import Dealer
POSICOES = ["SB", "BB", "UTG", "MP", "CO", "BTN"]
ACOES = ['fold', 'check', 'call', 'bet', 'raise']
BARALHO = Baralho()
BB = 10
SB = BB/2
FICHAS_INICIAIS = 1000


random_player = RandomPlayer(fichas=FICHAS_INICIAIS)
ia = Ia(fichas=FICHAS_INICIAIS)
dealer = Dealer()
jogadores = [random_player, ia]
mesa = Mesa(bb=BB, jogadores=jogadores)
done = random_player.fichas == 0 and ia.fichas == 0 #Até alguem sobreviver

def setar_inicio(jogadores):
    dealer.define_posicoes(jogadores, POSICOES)
    jogadores = sorted(jogadores, key=lambda jogador: POSICOES.index(jogador.posicao))
    dealer.recolher_blinds(bb=BB, mesa=mesa, jogadores=jogadores, sb=SB)
    dealer.distribuir_cartas(jogadores, BARALHO)

def rodada_apostas():
    dealer.apostas_pre_flop(jogadores, mesa)
    dealer.apostas_flop()
    dealer.apostas_turn()
    dealer.apostas_river()

while not done:
    setar_inicio(jogadores)
    rodada_apostas()
    print(BARALHO)
    done = True