print(">>> JOGO SUPER TRUNFO <<<")

print("REGRAS:\n")
print("- Cada país será dividido em 8 estados (identificadas pelas letras A a H).")
print("- Cada estado terá 4 cidades (numerados de 1 a 4).")
print("- A combinação de letras e números formarão o código da carta.")
print("EXEMPLO: A01; A02; B01; B02...\n")

# DADOS DA CARTA 1:

print("\nCADASTRO DA CARTA 1:\n")

estado_1 = str(input("Estado (A a H): ")).strip().upper()
cidade_1 = int(input("Código da carta (1 - 4): "))
nome_1 = str(input("Nome da Cidade: ")).strip().upper()
area_1 = float(input("Área da cidade (Km²): "))
populacao_1 = int(input("População: "))
pib_1 = float(input("PIB: R$"))
pontos_turisticos_1 = int(input("Pontos Turisticos: "))

densidade_populacional_1 = populacao_1 / area_1
pib_per_capita_1 = pib_1 / populacao_1

super_poder_1 = populacao_1 + area_1 + pib_1 + pontos_turisticos_1 + pib_per_capita_1 + (1 / densidade_populacional_1)

# DADOS DA CARTA 2:

print("\nCADASTRO DA CARTA 2:\n")

estado_2 = str(input("Estado (A a H): ")).strip().upper()
cidade_2 = int(input("Código da carta (1 - 4): "))
nome_2 = str(input("Nome da Cidade: ")).strip().upper()
area_2 = float(input("Área da cidade (Km²): "))
populacao_2 = int(input("População: "))
pib_2 = float(input("PIB: R$"))
pontos_turisticos_2 = int(input("Pontos Turisticos: "))

densidade_populacional_2 = populacao_2 / area_2
pib_per_capita_2 = pib_2 / populacao_2

super_poder_2 = populacao_2 + area_2 + pib_2 + pontos_turisticos_2 + pib_per_capita_2 + (1 / densidade_populacional_2)

# EXIBIÇAO DA CARTA 1:

print("\nDADOS DA CARTA 1\n")
print(f"CÓDIGO DA CARTA: {estado_1}0{cidade_1}")
print(f"Nome da Cidade: {nome_1}")
print(f"Área: {area_1}Km²")
print(f"População: {populacao_1}")
print(f"PIB: R${pib_1:,.2f} BILHÕES")
print(f"Pontos Turisticos: {pontos_turisticos_1}")
print(f"Densidade Populacional: {densidade_populacional_1:.1f} hab/Km²")
print(f"PIB per Capita: R${pib_per_capita_1:,.2f}")
print(f"Super Poder: {super_poder_1:.2f}")

# EXIBIÇAO DA CARTA 2:

print("\nDADOS DA CARTA 2\n")
print(f"CÓDIGO DA CARTA: {estado_2}0{cidade_2}")
print(f"Nome da Cidade: {nome_2}")
print(f"Área: {area_2}Km²")
print(f"População: {populacao_2}")
print(f"PIB: R${pib_2:,.2f} BILHÕES")
print(f"Pontos Turisticos: {pontos_turisticos_2}")
print(f"Densidade Populacional: {densidade_populacional_2:.1f} hab/Km²")
print(f"PIB per Capita: R${pib_per_capita_2:,.2f}")
print(f"Super Poder: {super_poder_2:.2f}")

# MENU INTERATIVO
for c in range(0, 2):
    
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
            print("\n>>> POPULAÇÃO <<<\n")
            print(f"CARTA 1 ({nome_1}): {populacao_1}")
            print(f"CARTA 2 ({nome_2}): {populacao_2}")
            if populacao_1 == populacao_2:
                print(f"\n>>> EMPATE! <<<")
            else:
                print(f"\nCARTA {1 if populacao_1 > populacao_2 else 2} VENCEU!")

        case 2:
            print("\n>>> ÁREA <<<\n")
            print(f"CARTA 1 ({nome_1}): {area_1} Km²")
            print(f"CARTA 2 ({nome_2}): {area_2} Km²")
            if area_1 == area_2:
                print(f"\n>>> EMPATE! <<<")
            else:
                print(f"\nCARTA {1 if area_1 > area_2 else 2} VENCEU!")

        case 3:
            print("\n>>> PIB <<<\n")
            print(f"CARTA 1 ({nome_1}): R${pib_1:,.2f} BILHÕES")
            print(f"CARTA 2 ({nome_2}): R${pib_2:,.2f} BILHÕES")
            if pib_1 == pib_2:
                print(f"\n>>> EMPATE! <<<")
            else:
                print(f"\nCARTA {1 if pib_1 > pib_2 else 2} VENCEU!")

        case 4:
            print("\n>>> PONTOS TURISTICOS <<<\n")
            print(f"CARTA 1 ({nome_1}): {pontos_turisticos_1}")
            print(f"CARTA 2 ({nome_2}): {pontos_turisticos_2}")
            if pontos_turisticos_1 == pontos_turisticos_2:
                print(f"\n>>> EMPATE! <<<")
            else:
                print(f"\nCARTA {1 if pontos_turisticos_1 > pontos_turisticos_2 else 2} VENCEU!")

        case 5:
            print("\n>>> DENSIDADE POPULACIONAL <<<\n")
            print(f"CARTA 1 ({nome_1}): {densidade_populacional_1:.1f} hab/Km²")
            print(f"CARTA 2 ({nome_2}): {densidade_populacional_2:.1f} hab/Km²")
            if densidade_populacional_1 == densidade_populacional_2:
                print(f"\n>>> EMPATE! <<<")
            else:
                print(f"\nCARTA {1 if densidade_populacional_1 < densidade_populacional_2 else 2} VENCEU!")

        case 6:
            print("\n>>> PIB PER CAPITA <<<\n")
            print(f"CARTA 1 ({nome_1}): R${pib_per_capita_1:,.2f}")
            print(f"CARTA 2 ({nome_2}): R${pib_per_capita_2:,.2f}")
            if pib_per_capita_1 == pib_per_capita_2:
                print(f"\n>>> EMPATE! <<<")
            else:
                print(f"\nCARTA {1 if pib_per_capita_1 > pib_per_capita_2 else 2} VENCEU!")
        
        case 7:
            print("\n>>> SUPER PODER <<<\n")
            print(f"CARTA 1 ({nome_1}): {super_poder_1:.2f}")
            print(f"CARTA 2 ({nome_2}): {super_poder_2:.2f}")
            if super_poder_1 == super_poder_2:
                print(f"\n>>> EMPATE! <<<")
            else:
                print(f"\nCARTA {1 if super_poder_1 > super_poder_2 else 2} VENCEU!")
        
        case 0:
            print("\nPROGRAMA ENCERRADO.")

        case _:
            print("\nOPÇAO INVALIDA. TENTE NOVAMENTE!")

