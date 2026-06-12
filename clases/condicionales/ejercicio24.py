class Taquilla:
    def __init__(self, edad):
        self.edad = edad

    def calcular_costo(self):
        if self.edad < 4:
            return "Puede entrar gratis"
        elif self.edad >= 4 and self.edad <= 18:
            return "El costo de acceso es de 5€"
        else:
            return "El costo de acceso es de 10€"
