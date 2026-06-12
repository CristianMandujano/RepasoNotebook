class VerificadorPrimos:
    def __init__(self):
        """Inicializa la clase pidiendo un número entero."""
        self.numero = int(input("Introduce un número entero: "))

    def es_primo(self) -> bool:
        """Determina si el número es primo usando un ciclo."""
        if self.numero <= 1:
            return False

        for i in range(2, self.numero):
            if self.numero % i == 0:
                return False  

        return True 

    def mostrar_resultado(self):
        """Muestra de forma clara el veredicto en la pantalla."""
        if self.es_primo():
            print(f"El número {self.numero} es primo.")
        else:
            print(f"El número {self.numero} no es primo.")

