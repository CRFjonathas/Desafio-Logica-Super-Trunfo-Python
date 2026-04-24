from classes.Carta import Carta


class Jogo:
    def __init__(self, carta1: Carta, carta2: Carta):
        self.carta1 = carta1
        self.carta2 = carta2

    def comparar(self, atributo: str) -> str:
        v1 = getattr(self.carta1, atributo)
        v2 = getattr(self.carta2, atributo)
        
        # densidade: menor vence
        if atributo == 'densidade_populacional':
            if v1 == v2:
                resultado = "EMPATE!"
            elif v1 < v2:
                resultado =  "CARTA 1 VENCEU!"
            else:
                resultado = "CARTA 2 VENCEU!"
        else:
            if v1 == v2:
                resultado = "EMPATE!"
            elif v1 > v2:
                resultado = "CARTA 1 VENCEU!"
            else:
                resultado = "CARTA 2 VENCEU!"
        
        return (f"\n>>> {atributo} <<<\n"
                f"\nCARTA 1({self.carta1.nome}): {v1}\n"
                f"CARTA 2({self.carta2.nome}): {v2}\n"
                f"\n--- {resultado} ---")