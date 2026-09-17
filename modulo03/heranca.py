from classes_objetos import Carro

class Caminhonete(Carro):
    def __init__(self, roda, motor, cor, modelo, cacamba):
        self.cacamba = cacamba
        super().__init__(roda, motor, cor, modelo)

    def __str__(self):
        return super().__str__()

    def carregar(self):
        return f"Carregando..."

jeep = Caminhonete(motor=2.4, cor="laranja", modelo="jeep", cacamba=500, roda=6)
print(jeep.carregar())