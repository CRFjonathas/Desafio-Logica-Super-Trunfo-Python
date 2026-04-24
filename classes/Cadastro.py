from classes.Carta import Carta


class Cadastrar:
    def cadastrar_carta() -> Carta:
        print("\nCADASTRO DA CARTA:\n")

        estado = str(input("Estado (A a H): ")).strip().upper()
        codigo = int(input("Código da carta (1 - 4): "))
        nome = str(input("Nome da Cidade: ")).strip().upper()
        populacao = int(input("População: "))
        area = float(input("Área da cidade (Km²): "))
        pib = float(input("PIB: R$"))
        pontos_turisticos = int(input("Pontos Turisticos: "))

        return Carta(estado, codigo, nome, populacao, area, pib, pontos_turisticos)