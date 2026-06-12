from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

from clases_load.load_basicos import DialogoEjercicio1
from clases_load.load_basicos import DialogoEjercicio2
from clases_load.load_basicos import DialogoEjercicio3
from clases_load.load_condicionales import DialogoEjercicio4
from clases_load.load_ciclos import DialogoEjercicio5
from clases_load.load_ciclos import DialogoEjercicio6
from clases_load.load_ciclos import DialogoEjercicio7
from clases_load.load_ciclos import DialogoEjercicio8
from clases_load.load_ciclos import DialogoEjercicio9
from clases_load.load_ciclos import DialogoEjercicio10
from clases_load.load_ciclos import DialogoEjercicio11
from clases_load.load_ciclos import DialogoEjercicio12
from clases_load.load_ciclos import DialogoEjercicio13
from clases_load.load_condicionales import DialogoEjercicio14
from clases_load.load_ciclos import DialogoEjercicio15
from clases_load.load_ciclos import DialogoEjercicio16
from clases_load.load_condicionales import DialogoEjercicio17
from clases_load.load_condicionales import DialogoEjercicio18
from clases_load.load_ciclos import DialogoEjercicio19
from clases_load.load_condicionales import DialogoEjercicio20
from clases_load.load_ciclos import DialogoEjercicio21
from clases_load.load_ciclos import DialogoEjercicio22
from clases_load.load_ciclos import DialogoEjercicio23
from clases_load.load_condicionales import DialogoEjercicio24  
from clases_load.load_ciclos import DialogoEjercicio25

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/menu_principal.ui", self)
        
        self.action_ejercicio1.triggered.connect(self.abrir_ejercicio1)
        self.action_ejercicio2.triggered.connect(self.abrir_ejercicio2)
        self.action_ejercicio3.triggered.connect(self.abrir_ejercicio3)
        self.action_ejercicio4.triggered.connect(self.abrir_ejercicio4)
        self.action_ejercicio5.triggered.connect(self.abrir_ejercicio5)
        self.action_ejercicio6.triggered.connect(self.abrir_ejercicio6)
        self.action_ejercicio7.triggered.connect(self.abrir_ejercicio7)
        self.action_ejercicio8.triggered.connect(self.abrir_ejercicio8)
        self.action_ejercicio9.triggered.connect(self.abrir_ejercicio9)
        self.action_ejercicio10.triggered.connect(self.abrir_ejercicio10)
        self.action_ejercicio11.triggered.connect(self.abrir_ejercicio11)
        self.action_ejercicio12.triggered.connect(self.abrir_ejercicio12)
        self.action_ejercicio13.triggered.connect(self.abrir_ejercicio13)
        self.action_ejercicio14.triggered.connect(self.abrir_ejercicio14)
        self.action_ejercicio15.triggered.connect(self.abrir_ejercicio15)
        self.action_ejercicio16.triggered.connect(self.abrir_ejercicio16)
        self.action_ejercicio17.triggered.connect(self.abrir_ejercicio17)
        self.action_ejercicio18.triggered.connect(self.abrir_ejercicio18)
        self.action_ejercicio19.triggered.connect(self.abrir_ejercicio19)
        self.action_ejercicio20.triggered.connect(self.abrir_ejercicio20)
        self.action_ejercicio21.triggered.connect(self.abrir_ejercicio21)
        self.action_ejercicio22.triggered.connect(self.abrir_ejercicio22)
        self.action_ejercicio23.triggered.connect(self.abrir_ejercicio23)
        self.action_ejercicio24.triggered.connect(self.abrir_ejercicio24)
        self.action_ejercicio25.triggered.connect(self.abrir_ejercicio25)
        self.action_salir.triggered.connect(self.close)

    def abrir_ejercicio1(self):
        ventana_ej1 = DialogoEjercicio1()
        ventana_ej1.exec_()

    def abrir_ejercicio2(self):
        ventana_ej2 = DialogoEjercicio2()
        ventana_ej2.exec_()

    def abrir_ejercicio3(self):
        ventana_ej3 = DialogoEjercicio3()
        ventana_ej3.exec_()

    def abrir_ejercicio4(self):
        ventanaej4 = DialogoEjercicio4()
        ventanaej4.exec_()

    def abrir_ejercicio6(self):
        ventana_ej6 = DialogoEjercicio6()
        ventana_ej6.exec_() 

    def abrir_ejercicio7(self):
        ventana_ej7 = DialogoEjercicio7()
        ventana_ej7.exec_()

    def abrir_ejercicio8(self):
        ventana_ej8 = DialogoEjercicio8()
        ventana_ej8.exec_()

    def abrir_ejercicio9(self):
        ventana_ej9 = DialogoEjercicio9()
        ventana_ej9.exec_()
    
    def abrir_ejercicio10(self):
        ventana_ej10 = DialogoEjercicio10()
        ventana_ej10.exec_()

    def abrir_ejercicio11(self):
        ventana_ej11 = DialogoEjercicio11()
        ventana_ej11.exec_()

    def abrir_ejercicio12(self):        
        ventana_ej12 = DialogoEjercicio12()
        ventana_ej12.exec_()

    def abrir_ejercicio13(self):
        ventana_ej13 = DialogoEjercicio13()
        ventana_ej13.exec_()

    def abrir_ejercicio14(self):
        ventana_ej14 = DialogoEjercicio14()
        ventana_ej14.exec_()

    def abrir_ejercicio15(self):
        ventana_ej15 = DialogoEjercicio15()
        ventana_ej15.exec_()

    def abrir_ejercicio16(self):
        ventana_ej16 = DialogoEjercicio16()
        ventana_ej16.exec_()

    def abrir_ejercicio17(self):
        ventana_ej17 = DialogoEjercicio17()
        ventana_ej17.exec_()

    def abrir_ejercicio18(self):
        ventana_ej18 = DialogoEjercicio18()
        ventana_ej18.exec_()

    def abrir_ejercicio19(self):
        ventana_ej19 = DialogoEjercicio19()
        ventana_ej19.exec_()

    def abrir_ejercicio20(self):
        ventana_ej20 = DialogoEjercicio20()
        ventana_ej20.exec_()

    def abrir_ejercicio21(self):
        ventana_ej21 = DialogoEjercicio21()
        ventana_ej21.exec_()

    def abrir_ejercicio22(self):
        ventana_ej22 = DialogoEjercicio22()
        ventana_ej22.exec_()

    def abrir_ejercicio23(self):
        ventana_ej23 = DialogoEjercicio23()
        ventana_ej23.exec_()

    def abrir_ejercicio24(self):
        ventana_ej24 = DialogoEjercicio24()
        ventana_ej24.exec_()

    def abrir_ejercicio25(self):
        ventana_ej25 = DialogoEjercicio25()
        ventana_ej25.exec_()

    
