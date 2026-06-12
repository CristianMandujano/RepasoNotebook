from clases.basicos.ejercicio1 import Recta
from clases.basicos.ejercicio2 import Coordenadas
from clases.basicos.ejercicio3 import Distribucion 

class Basicos(object):
    def __init__(self):  
        self.opcion = 0

    def mostrar_menu_basicos(self):
        print("---- MENU BASICOS ----")
        print("1. Pendiente de una recta")
        print("2. Distancia de dos puntos ")
        print("3. Calcular funcion")
        print("4. Volver al menu principal")
        
    def leer_ejecutar_opcion(self):
        self.opcion = int(input("Selecione una opcion:"))
        match self.opcion:
            case 1:
                figura = Recta(0, 0, 0, 0)
                figura.leer_datos()
                figura.calcular_pendiente()
                figura.imprimir_pendiente()
            case 2:
                puntos = Coordenadas()
                puntos.leerDatos()
                puntos.calcularDistancia()
                puntos.imprimirDistancia()
            case 3:
                calculadora = Distribucion(0, 0, 0)
                calculadora.leer_datos() 
                
                resultado = calculadora.calcular_fx()
                print(f"fx={resultado}")
            case 4:
                print("Saliendo al menú principal")

    def ejecutar(self):
        while self.opcion != 4:
            self.mostrar_menu_basicos()
            self.leer_ejecutar_opcion()