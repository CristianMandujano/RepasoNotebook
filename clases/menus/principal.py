from menus.basicos import Basicos 

class Principal(object):
    def __init__(self):
        self.opcion = 0

    def mostar_menu_principal(self):
        print("---- MENU PRINCIPAL ----")
        print("1. Basicos")
        print("2. Ciclos")
        print("3. Condicionales ")
        #Pendiente de agregar opciones para cada tema
        print("5. Salir")

    def leer_ejecutar_opcion(self):
        self.opcion = int(input("Seleccione una opcion: "))
        match self.opcion:
            case 1:
                basicos = Basicos()
                basicos.ejecutar()

    def ejecutar(self):
        while self.opcion != 5:
            self.mostar_menu_principal()
            self.leer_ejecutar_opcion()