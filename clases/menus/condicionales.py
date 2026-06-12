from clases.condicionales.ejercicio4 import Circulo
from clases.condicionales.ejercicio14 import VerificadorPrimos
from clases.condicionales.ejercicio17 import Divisor
from clases.condicionales.ejercicio18 import AsignadorGrupos
from clases.condicionales.ejercicio20 import CalculadoraIMC
from clases.condicionales.ejercicio24 import Taquilla

class Condicionales(object):
    def __init__(self):
        self.opcion = 0

    def mostrar_menu_condicionales(self):
        print("\n" + "-"*30)
        print("    MENU CONDICIONALES")
        print("-"*30)
        print("1. Calcular distancia")
        print("2. Verificar numeros primos")
        print("3. Divisor")
        print("4. Asignar grupos")
        print("5. Calcula tu IMC")
        print("6. Calcula el costo de taquilla")
        print("7. Volver al menu principal")
        print("-"*30)

    def leer_ejecutar_opcion(self):
        try:
            self.opcion = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            self.opcion = 0
            return

        match self.opcion:
            case 1:
                figure = Circulo()
                figure.leer_datos()
                figure.calcular_distancia()
                figure.imprimir_resultado()
            case 2:
                programa_14 = VerificadorPrimos()
                programa_14.mostrar_resultado()
            case 3:
                operacion = Divisor()
                operacion.realizar_division()
            case 4:                
                sistema = AsignadorGrupos()
                sistema.determinar_grupo()
            case 5:
                paciente = CalculadoraIMC()
                paciente.obtener_diagnostico()
            case 6:
                cliente = Taquilla()
                cliente.calcular_costo()
            case 7:
                print("Regresando al menú principal...")
            case _:
                print("Opción inválida. Intente de nuevo.")

    def ejecutar(self):
        while self.opcion != 7:
            self.mostrar_menu_condicionales()
            self.leer_ejecutar_opcion()

        


                






