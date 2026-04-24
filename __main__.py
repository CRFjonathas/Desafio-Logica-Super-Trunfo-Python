from classes.Cadastro import Cadastrar
from classes.Baralho import Baralho    

def main():
    baralho = Baralho()

    carta1 = Cadastrar.cadastrar_carta() 
    baralho.adicionar_carta(carta1)

    carta2 = Cadastrar.cadastrar_carta()
    baralho.adicionar_carta(carta2)

    for cartas in baralho:
        print(cartas) 

if __name__ == "__main__":
    main()