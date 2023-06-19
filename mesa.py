class Mesa:
    def __init__(self, bb, jogadores):
        self.bb = bb
        self.sb = bb/2
        self.jogadores = jogadores
        self.pote = 0
        self.ultima_aposta = bb