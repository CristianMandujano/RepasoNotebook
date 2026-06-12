import math

class Circulo:
  def __init__(self, x_centro, y_centro, radio):
    self.x_centro = x_centro
    self.y_centro = y_centro
    self.radio = radio
    self.x_punto = 0
    self.y_punto = 0

  def leer_datos(self):
    self.x_centro = int(input('x centro: '))
    self.y_centro = int(input('y centro: '))
    self.radio = int(input('radio: '))
    self.x_punto = int(input('x punto: '))
    self.y_punto = int(input('y punto: '))

  def calcular_distancia(self):
    return math.sqrt((self.x_punto - self.x_centro)**2 + (self.y_punto - self.y_centro)**2)

  def imprimir_resultado(self):
    distancia = self.calcular_distancia()
    if distancia > self.radio:
      print('El punto está fuera de la circunferencia')
    elif distancia < self.radio:
      print('El punto está dentro de la circunferencia')
    else:
      print('El punto está sobre la circunferencia')