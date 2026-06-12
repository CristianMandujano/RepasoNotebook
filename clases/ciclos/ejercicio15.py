class PalabraInversa:
    def __init__(self):
        """Inicializa la clase pidiendo la palabra al usuario."""
        self.palabra = input("Introduce una palabra: ")

    def mostrar_al_reves(self):
        """Recorre la palabra desde el último carácter hasta el primero usando un ciclo."""
        print("Letras al revés:")

        ultimo_indice = len(self.palabra) - 1

        for i in range(ultimo_indice, -1, -1):
            print(self.palabra[i])

programa_15 = PalabraInversa()
programa_15.mostrar_al_reves()