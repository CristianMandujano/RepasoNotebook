class Division:
  def __init__(self, num1=0, num2=0):
    self.num1 = num1
    self.num2 = num2

  def leer_datos(self):
    self.num1 = int(input("Ingrese el primer número entero: "))
    self.num2 = int(input("Ingrese el segundo número entero: "))

  def calcular_cociente_resto(self):
    if self.num2 == 0:
      return None, None 
    cociente = self.num1 // self.num2
    resto = self.num1 % self.num2
    return cociente, resto

  def imprimir_resultado(self):
    cociente, resto = self.calcular_cociente_resto()
    if cociente is None:
      print("¡Error! No se puede dividir por cero.")
    else:
      print(f"El valor de {self.num1} entre {self.num2} da un cociente de: {cociente} y un resto de: {resto}")

division_op = Division()
division_op.leer_datos()
division_op.imprimir_resultado()