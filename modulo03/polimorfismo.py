class Cavalo():
    def __init__(self, montaria):
        self.montaria = montaria

    def andar(self):
        return "Andando"

class Barco():
    def __init__(self, tipo):
        self.montaria = tipo

    def andar(self):
        return "Andando"

class Aviao():
    def __init__(self, agencia):
        self.montaria = agencia

    def andar(self):
        return "Andando"
