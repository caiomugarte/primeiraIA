class Baralho:
    def __init__(self) -> None:
        naipes = ["♠", "♥", "♦", "♣"]
        valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        cartas = [valor + naipe for valor in valores for naipe in naipes]
        self.cartas = cartas;