import math

class SumatoriaGeometrica:
  def __init__(self, n):
    self.n = n

  def leer_datos(self):
    self.n = int(input('n = '))

  def calcular_sumatoria(self):
    sum_val = 0
    for k in range(1, self.n + 1):
      sum_val += (1 / math.e)**k
    return (1/3) * sum_val

  def imprimir_resultado(self):
    print(f'n = {self.n}, serie = {self.calcular_sumatoria()}')

