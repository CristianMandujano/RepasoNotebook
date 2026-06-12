class ImparesConsecutivos:
    def __init__(self):
        """Inicializa la clase solicitando el número límite."""
        self.numero = int(input("Ingresa un número entero positivo: "))

    def mostrar_impares(self):
        """Filtra los números impares y los muestra separados por comas."""
        impares = []

        for i in range(1, self.numero + 1, 2):
            impares.append(str(i))

        resultado = ", ".join(impares)
        print(resultado)

programa_11 = ImparesConsecutivos()
programa_11.mostrar_impares()