class TablaMultiplicar:
  def __init__(self, numero=0):
    self.numero = numero

  def leer_numero(self):
    self.numero = int(input('Introduce un número para su tabla de multiplicar: '))

  def generar_tabla(self):
    print(f'\nTabla de multiplicar del {self.numero}:')
    for i in range(1, 11): # From 1 to 10
      print(f'{self.numero} x {i} = {self.numero * i}')

tabla = TablaMultiplicar()
tabla.leer_numero()
tabla.generar_tabla()