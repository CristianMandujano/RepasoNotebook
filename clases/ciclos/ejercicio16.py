class ContadorLetras:
    def __init__(self, frase, letra):
        self.frase = frase
        self.letra = letra

    def contar(self):
        contador = 0
        for caracter in self.frase:
            if caracter == self.letra:
                contador += 1
        return contador

texto = input("Introduce una frase: ")
caracter_buscar = input("Introduce una letra: ")

analizador = ContadorLetras(texto, caracter_buscar)
total = analizador.contar()

print(f"La letra {caracter_buscar} aparece {total} veces en la frase")