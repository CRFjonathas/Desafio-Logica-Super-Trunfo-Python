class Carta:
    def __init__(self, estado, codigo, nome, populacao, area, pib, pontos_turisticos):
        self.estado = estado
        self.codigo = codigo
        self.nome = nome
        self._populacao = populacao
        self._area = area
        self._pib = pib
        self.pontos_turisticos = pontos_turisticos


    @property
    def densidade_populacional(self):
        return self._populacao / self._area

    @property
    def pib_per_capita(self):
        return (self._pib * 1000000000) / self._populacao

    @property
    def super_poder(self):
        # regra: densidade menor vence, entao inverte
        return (self._populacao + self._area + (self._pib * 1000000000) + self.pontos_turisticos + self.pib_per_capita + (1 / self.densidade_populacional))

    def __str__(self):
        return f"""\n--- DADOS DA CARTA ---\n
Código da carta: {self.estado}0{self.codigo}
Cidade: {self.nome}
Área: {self._area}Km²
População: {self._populacao:,.0f}
PIB: R${self._pib:,.2f} BILHÕES
Pontos Turisticos: {self.pontos_turisticos}
Densidade Populacional: {self.densidade_populacional:.1f} hab/Km²
PIB per Capita: R${self.pib_per_capita:.2f}
Super Poder: {self.super_poder:.0f}"""

    def __repr__(self):
        return f"Carta(nome={self.nome!r}, estado={self.estado!r})"
