class carro:
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def exibir_informacoes(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Cor:", self.cor)
        print("Ano:", self.ano)

carro1 = carro("Toyota", "Corrola", "Prata", 2020)
carro2 = carro("Honda", "Civic", "Branco", 2019)

carro1.exibir_informacoes()
carro2.exibir_informacoes()

input()


