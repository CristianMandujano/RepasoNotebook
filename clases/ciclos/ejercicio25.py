class InversorFrase:
    def __init__(self, frase):
        self.frase = frase

    def invertir(self):
        return self.frase[::-1]

texto = input("Ingrese la frase: ")

procesador = InversorFrase(texto)
frase_invertida = procesador.invertir()

print(f"La frase invertida es: {frase_invertida}")