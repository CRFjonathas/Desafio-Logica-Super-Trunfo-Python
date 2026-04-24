from classes.Carta import Carta


class Baralho:
    def __init__(self):
        self._cartas = []

    def adicionar_carta(self, carta: Carta):
        self._cartas.append(carta)

    def __len__(self):
        return len(self._cartas)

    def __iter__(self):
        return iter(self._cartas)