from classes.Carta import Carta


class Jogo:
    def __init__(self, carta1: Carta, carta2: Carta):
        self.carta1 = carta1
        self.carta2 = carta2

    def comparar(self, atributo_interno: str) -> str:
        v1 = getattr(self.carta1, atributo_interno)
        v2 = getattr(self.carta2, atributo_interno)

        nomes_amigaveis = {
            "_populacao" : "População",
            "_area" : "Área",
            "_pib" : "PIB",
            "pontos_turisticos" : "Pontos Turisticos",
            "densidade_populacional" : "Densidade Populacional",
            "pib_per_capita" : "PIB Per Capita",
            "super_poder" : "Super Poder"
        }

        nome_exibicao = nomes_amigaveis.get(atributo_interno, atributo_interno)
        
        # densidade: menor vence
        if atributo_interno == 'densidade_populacional':
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
        
        return (f"\n>>> {nome_exibicao} <<<\n"
                f"\nCARTA 1({self.carta1.nome}): {v1}\n"
                f"CARTA 2({self.carta2.nome}): {v2}\n"
                f"\n--- {resultado} ---")