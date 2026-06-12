class CuentaAtras:
    def __init__(self, numero):
        self.numero = numero

    def generar_cuenta(self):
        numeros = []
        for i in range(self.numero, -1, -1):
            numeros.append(str(i))
        return ", ".join(numeros)

num_usuario = int(input("Introduce un número entero positivo: "))

if num_usuario >= 0:
    contador = CuentaAtras(num_usuario)
    resultado = contador.generar_cuenta()
    print(resultado)
else:
    print("Por favor, introduce un número positivo.")