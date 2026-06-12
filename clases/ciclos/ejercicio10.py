class ContadorEdad:
    def __init__(self):
        """Inicializa la clase solicitando la edad al usuario."""
        self.edad = int(input("¿Cuál es tu edad?: "))

    def mostrar_anios_cumplidos(self):
        """Muestra de forma estructurada los años cumplidos."""
        for i in range(1, self.edad + 1):
            if i == 1:
                print(f"Has cumplido {i} año")
            else:
                print(f"Has cumplido {i} años")

programa_10 = ContadorEdad()
programa_10.mostrar_anios_cumplidos()