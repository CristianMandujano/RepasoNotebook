class CuentaAhorros:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
        self.interes = 0.04

    def calcular_rendimientos(self):
        y1 = self.saldo * (1 + self.interes)
        y2 = y1 * (1 + self.interes)
        y3 = y2 * (1 + self.interes)
        return y1, y2, y3

deposito = float(input("Ingrese la cantidad de dinero depositada en la cuenta de ahorros: "))

cuenta = CuentaAhorros(deposito)
año1, año2, año3 = cuenta.calcular_rendimientos()

print(f"La cantidad de ahorros tras el primer año es: {round(año1, 2)}€")
print(f"La cantidad de ahorros tras el segundo año es: {round(año2, 2)}€")
print(f"La cantidad de ahorros tras el tercer año es: {round(año3, 2)}€")