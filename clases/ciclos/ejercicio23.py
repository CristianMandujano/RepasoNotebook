class CalculadoraPan:
    def __init__(self, cantidad_barras):
        self.precio_habitual = 3.49
        self.descuento = self.precio_habitual * 0.6
        self.cantidad = cantidad_barras

    def calcular_total(self):
        return self.cantidad * self.descuento

barras_viejas = int(input("Ingrese la cantidad de barras vendidas que no son del día: "))

venta = CalculadoraPan(barras_viejas)

print(f"El precio habitual de una barra de pan es: {venta.precio_habitual}€")
print(f"El descuento que se le hace por no ser fresca es: {venta.descuento}€")
print(f"El coste final total es: {venta.calcular_total()}€")