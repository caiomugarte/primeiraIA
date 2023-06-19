import random
from jogador import Jogador
from mesa import Mesa
from baralho import Baralho
class Dealer:
    QTD_CARTAS = 2
    def processa_acao(self, jogador: Jogador, mesa: Mesa):
        acao = jogador.get_acao()
        if(acao == "call"):
            jogador.fichas -= mesa.ultima_aposta
            mesa.pote += mesa.ultima_aposta
        if(acao == "raise"):
            jogador.fichas -= jogador.get_raise(mesa.ultima_aposta)
            mesa.pote += jogador.get_raise(mesa.ultima_aposta)
            
            

    def get_acoes_validas(self, jogador: Jogador, mesa: Mesa):
        acoes = ['fold']
        if(jogador.fichas)
    
    def apostas_pre_flop(self, jogadores: list, mesa: Mesa):
        jogador: Jogador
        for jogador in jogadores:
            jogador.acoes_possiveis = self.get_acoes_validas(jogador, mesa)
            self.processa_acao(jogador, mesa)

    def distribuir_cartas(self, jogadores: list, baralho: Baralho):
        random.shuffle(baralho.cartas)
        for _ in range(self.QTD_CARTAS):
            for jogador in jogadores:
                carta = baralho.cartas.pop()
                jogador.cartas.append(carta)

        
    def recolher_blinds(self, mesa: Mesa, jogadores: list, bb, sb):
        jogador: Jogador
        for jogador in jogadores:
            if(jogador.posicao == "BB"):
                jogador.fichas -= bb
            if(jogador.posicao == "SB"):
                jogador.fichas -= sb
        mesa.pote += bb + sb
    def define_posicoes(self, jogadores: list, posicoes: list):
        for i, jogador in enumerate(jogadores):
            jogador.posicao = posicoes[i]; 
        
            

