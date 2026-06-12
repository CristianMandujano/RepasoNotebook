class CalculadoraInversion:
    def __init__(self):
        """Inicializa la clase solicitando los datos financieros al usuario."""
        self.cantidad = float(input("Cantidad a invertir: "))
        self.interes = float(input("Interés anual (%): "))
        self.anios = int(input("Número de años: "))

    def calcular_rendimientos(self):
        """Calcula y muestra el capital acumulado año por año."""
        print("\n--- Evolución de la Inversión ---")
        for i in range(1, self.anios + 1):
            capital = self.cantidad * (1 + self.interes / 100) ** i
            print(f"Año {i}: {capital:.2f}")

programa_13 = CalculadoraInversion()
programa_13.calcular_rendimientos()