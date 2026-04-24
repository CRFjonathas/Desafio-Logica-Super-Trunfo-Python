from classes.Cadastrar import Cadastrar
from classes.Baralho import Baralho
from classes.Jogo import Jogo
from classes.Menu import Menu


def main():
    baralho = Baralho()

    carta1 = Cadastrar.cadastrar_carta() 
    baralho.adicionar_carta(carta1)

    carta2 = Cadastrar.cadastrar_carta()
    baralho.adicionar_carta(carta2)

    for cartas in baralho:
        print(cartas) 

    comparacao = Jogo(carta1, carta2)

    for c in range(0,2):
        print(Menu.selecionar(comparacao))

if __name__ == "__main__":
    main()