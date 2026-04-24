from classes.Jogo import Jogo


class Menu:
    @staticmethod
    def selecionar(jogo) -> Jogo:
        print("\nSELECIONE O ATRIBUTO QUE VOCÊ QUER COMPARAR\n")
        print("1. POPULAÇÃO")
        print("2. ÁREA")
        print("3. PIB")
        print("4. PONTOS TURISTICOS")
        print("5. DENSIDADE POPULACIONAL")
        print("6. PIB PER CAPITA")
        print("7. SUPER PODER")
        print("0. SAIR\n")

        opcao = int(input("-> "))

        match opcao:
            case 1:
                print(jogo.comparar("_populacao"))
            case 2:
                print(jogo.comparar("_area"))
            case 3:
                print(jogo.comparar("_pib"))
            case 4:               
                print(jogo.comparar("pontos_turisticos"))
            case 5:
                print(jogo.comparar("densidade_populacional"))
            case 6:                
                print(jogo.comparar("pib_per_capita"))
            case 7:
                print(jogo.comparar("super_poder"))
            case 0:
                print("\nPROGRAMA ENCERRADO.")
            case _:
                print("\nOPÇAO INVALIDA!")