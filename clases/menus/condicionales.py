from clases.condicionales.ejercicio4 import Circulo
from clases.condicionales.ejercicio14 import VerificadorPrimos
from clases.condicionales.ejercicio17 import Divisor
from clases.condicionales.ejercicio18 import AsignadorGrupos
from clases.condicionales.ejercicio20 import CalculadoraIMC
from clases.condicionales.ejercicio24 import Taquilla

class Condicionales(object):
    def __init__(self):
        self.opcion=0

    def mostrar_menu_condicionales(self):
        print("---- MENU CONDICIONALES ----")
        print("1. Calcular distancia ")
        print("2. Verificar numeros primos ")
        print("3. Divisor ")
        print("4. Asignar grupos ")
        print("5. Calcula tu IMC ")
        print("6. Calcula el costo de taquilla ")
        print("7. Volver al menu principal")

    def leer_ejecutar_opcion(self):
        self.opcion= int(input("Seleccione una opcion: "))
        match self.opcion:
            case 1:
                figure=Circulo()
                figure.leer_datos()
                



