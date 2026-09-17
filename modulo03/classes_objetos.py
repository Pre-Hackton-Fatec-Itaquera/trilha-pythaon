class Carro:
    def __init__(self, roda, motor, cor, modelo):
        self.roda = roda
        self.motor = motor
        self.cor = cor
        self.modelo = modelo

    def __str__(self):
        return f"{self.modelo}, {self.motor}, {self.cor}"

    def parada(self):
        return "Vi um lanche daora, bora parar"

    def senna(self):
        return "Curvas adiante, vamos freiar"

azuzinho = Carro(roda=35, motor=1.6, cor="azul", modelo="hatch")
amarelinho = Carro(roda=35, motor=1.6, cor="amarelo", modelo="hatch")
verdoca = Carro(roda=35, motor=1.6, cor="verde", modelo="hatch")
cinzeiro = Carro(roda=35, motor=1.6, cor="cinza", modelo="hatch")

print(cinzeiro.parada())
print(amarelinho.senna())

print(f"{azuzinho}\n{amarelinho}\n{verdoca}\n{cinzeiro}")