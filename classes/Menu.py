class Menu:
    @staticmethod
    def selecionar(jogo) -> str:
        atributos = {
            1: "_populacao",
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

        try:
            opcao = int(input("-> "))
        except ValueError:
            return "OPÇÃO INVÁLIDA! Por favor, digite apenas números."
        
        if opcao == 0:
            return "PROGRAMA ENCERRADO!"

        atributo = atributos.get(opcao)

        if atributo is not None:
            return jogo.comparar(atributo)
        else:
            return "OPÇÃO INVALIDA!"