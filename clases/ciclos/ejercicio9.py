class RepetidorPalabra:
  def __init__(self, palabra=""):
    self.palabra = palabra

  def pedir_palabra(self):
    self.palabra = input('Introduce una palabra: ')

  def mostrar_diez_veces(self):
    for _ in range(10):
      print(self.palabra)
