from classes.Carta import Carta, Cadastrar
    

def main():
    carta1 = Cadastrar.cadastrar_carta()
    carta2 = Cadastrar.cadastrar_carta()

    print(carta1)
    print(carta2)

if __name__ == "__main__":
    main()