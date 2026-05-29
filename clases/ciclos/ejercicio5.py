import math

class Sumatoria:
  def __init__(self, n):
    self.n = n

  def leer_datos(self):
    self.n = int(input('n = '))

  def calcular_sumatoria(self):
    sum_val = 0
    for i in range(1, self.n + 1):
      sum_val += 1 / math.sqrt((2 * i + 1)**2)
    return sum_val

  def imprimir_resultado(self):
    print(f'n = {self.n}, serie = {self.calcular_sumatoria()}')

# Caso de prueba 1
sumatoria1 = Sumatoria(5)
print('Caso de prueba 1:')
sumatoria1.imprimir_resultado()

# Caso de prueba 2
sumatoria2 = Sumatoria(8)
print('\nCaso de prueba 2:')
sumatoria2.imprimir_resultado()
