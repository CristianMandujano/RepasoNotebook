class CalculadoraIMC:
    def __init__(self, peso, estatura):
        self.peso = float(peso)
        self.estatura = float(estatura)

    def obtener_diagnostico(self):
        imc = round(self.peso / (self.estatura ** 2), 2)
        
        if imc < 18.5:
            return imc, "Estas en bajo peso"
        elif imc >= 18.5 and imc <= 24.9:
            return imc, "Estas en peso normal"
        elif imc >= 25 and imc <= 29.9:
            return imc, "Estas en sobrepeso"
        else:
            return imc, "Estas en obesidad"
