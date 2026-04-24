from classes.Jogo import Jogo


class Menu:
    @staticmethod
    def selecionar(jogo) -> Jogo:
        atributos = {
            1: "_populcao",
            2: "_area",
            3: "_pib",
            4: "pontos_turisticos",
            5: "densidade_populacional",
            6: "pib_per_capita",
            7: "super_poder"
        }


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
        
        if opcao == 0:
            return "PROGRAMA ENCERRADO!"

        atributo = atributos.get(opcao)

        if atributo is not None:
            return jogo.comparar(atributo)
        elif atributo is None:
            return "OPÇÃO INVALIDA!"