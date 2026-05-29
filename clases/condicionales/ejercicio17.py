class Divisor:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def realizar_division(self):
        if self.num2 == 0:
            return "¡Error! No se puede dividir por cero"
        else:
            return f"{self.num1} / {self.num2} = {self.num1 / self.num2}"

n1 = int(input("¿Cuál es el primer número? "))
n2 = int(input("¿Cuál es el segundo número? "))

operacion = Divisor(n1, n2)
resultado = operacion.realizar_division()

print(resultado)