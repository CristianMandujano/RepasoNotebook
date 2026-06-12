from clases.ciclos.ejercicio5 import Sumatoria
from clases.ciclos.ejercicio6 import SumatoriaGeometrica
from clases.ciclos.ejercicio7 import TablaMultiplicar
from clases.ciclos.ejercicio8 import TablaMultiplicar1_10
from clases.ciclos.ejercicio9 import RepetidorPalabra
from clases.ciclos.ejercicio10 import ContadorEdad
from clases.ciclos.ejercicio11 import ImparesConsecutivos
from clases.ciclos.ejercicio12 import CuentaAtras
from clases.ciclos.ejercicio13 import CalculadoraInversion  
from clases.ciclos.ejercicio15 import PalabraInversa
from clases.ciclos.ejercicio16 import ContadorLetras
from clases.ciclos.ejercicio19 import Saludador
from clases.ciclos.ejercicio21 import Division
from clases.ciclos.ejercicio22 import CuentaAhorros
from clases.ciclos.ejercicio23 import CalculadoraPan
from clases.ciclos.ejercicio25 import InversorFrase


class Ciclos(object):
    def __init__(self):
        # Inicializamos la variable en un valor neutro (como 0) para controlar el ciclo while
        self.opcion = 0

    def mostrar_menu_ciclos(self):
        # Separamos el menú para que se imprima cada vez que termine un ejercicio
        print("\n" + "="*35)
        print("         MENÚ DE CICLOS")
        print("="*35)
        print("1. Sumatoria\n2. Sumatoria Geométrica\n3. Tabla Multiplicar\n4. Tabla Multiplicar 1-10")
        print("5. Repetidor Palabra\n6. Contador Edad\n7. Impares Consecutivos\n8. Cuenta Atrás")
        print("9. Calculadora Inversión\n10. Palabra Inversa\n11. Contador Letras\n12. Saludador")
        print("13. División\n14. Cuenta Ahorros\n15. Calculadora Pan\n16. Inversor Frase")
        print("17. Salir")
        print("="*35)
        
        try:
            self.opcion = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            self.opcion = 0

    def leer_ejecutar_opcion(self):
        # Todo tu bloque match-case se ejecuta de forma segura aquí
        match self.opcion:
            case 1:
                operacion = Sumatoria()
                operacion.leer_datos()
                operacion.calcular_sumatoria()
                operacion.imprimir_resultado()
            case 2:
                Opgeo = SumatoriaGeometrica()
                Opgeo.calcular_sumatoria()
                Opgeo.imprimir_resultado()
            case 3:
                tablas = TablaMultiplicar()
                tablas.leer_numero()
                tablas.generar_tabla()
            case 4:
                tabla = TablaMultiplicar1_10()
                tabla.leer_numero()
                tabla.generar_tabla()
            case 5:
                palabra = RepetidorPalabra()
                palabra.pedir_palabra()
                palabra.mostrar_diez_veces()
            case 6:
                edad = ContadorEdad()
                edad.mostrar_anios_cumplidos()
            case 7:
                impares = ImparesConsecutivos()
                impares.mostrar_impares()
            case 8:
                cuenta = CuentaAtras()
                cuenta.generar_cuenta()
            case 9:
                programa_13 = CalculadoraInversion()
                programa_13.calcular_rendimientos()
            case 10:               
                programa_15 = PalabraInversa()
                programa_15.mostrar_al_reves()
            case 11:
                contador = ContadorLetras()
                contador.contar()
            case 12:
                saludo = Saludador()
                saludo.dar_bienvenida()
            case 13:
                division_op = Division()
                division_op.leer_datos()
                division_op.imprimir_resultado()
            case 14:
                ahorrar = CuentaAhorros()
                ahorrar.calcular_rendimientos()
            case 15:
                pan = CalculadoraPan()
                pan.calcular_total()
            case 16:
                frase = InversorFrase()
                frase.invertir()
            case 17:
                print("Saliendo del menú de ciclos...")
            case _:
                print("Opción inválida.")

    def ejecutar(self):
        while self.opcion != 17:
            self.mostrar_menu_ciclos()
            if self.opcion != 17:
                self.leer_ejecutar_opcion()

if __name__ == "__main__":
    app = Ciclos()
    app.ejecutar()

                





