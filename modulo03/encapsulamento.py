class Carro:
  def __init__(self, nome, chave):
    self.nome = nome
    self.__chave = chave

  def pegar_chave(self):
    return self.__chave

opel = Carro("CorsaB", "chave_corsa")
print(opel.pegar_chave())