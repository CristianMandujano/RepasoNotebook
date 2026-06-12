from PyQt5.QtWidgets import QDialog
from PyQt5 import uic

from clases.basicos.ejercicio1 import Recta
from clases.basicos.ejercicio2 import Coordenadas
from clases.basicos.ejercicio3 import Distribucion

class DialogoEjercicio1(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/dialogo_ejercicio1.ui", self)
        
        self.btn_calcular.clicked.connect(self.procesar_ejercicio)

    def procesar_ejercicio(self):
        try:
            x1 = float(self.txt_x1.text())
            y1 = float(self.txt_y1.text())
            x2 = float(self.txt_x2.text())
            y2 = float(self.txt_y2.text())
            
            figura = Recta(x1, y1, x2, y2)
            figura.calcular_pendiente()
            pendiente = figura.pendiente
            
            self.lbl_resultado.setText(f"Pendiente de la recta: {pendiente:.6f}")
            
        except ValueError:
            self.lbl_resultado.setText("Por favor, ingresa valores numéricos válidos.")

class DialogoEjercicio2(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/dialogo_ejercicio2.ui", self)
        
        self.btn_calcular.clicked.connect(self.procesar_ejercicio)

    def procesar_ejercicio(self):
        try:
            x1 = float(self.txt_x1.text())
            y1 = float(self.txt_y1.text())
            x2 = float(self.txt_x2.text())
            y2 = float(self.txt_y2.text())
            
            puntos = Coordenadas(x1, y1, x2, y2)
            puntos.calcular_distancia()
            distancia = puntos.distancia
            
            self.lbl_resultado.setText(f"Distancia entre los puntos: {distancia:.6f}")
            
        except ValueError:
            self.lbl_resultado.setText("Por favor, ingresa valores numéricos válidos.") 

class DialogoEjercicio3(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/dialogo_ejercicio3.ui", self)
        
        self.btn_calcular.clicked.connect(self.procesar_ejercicio)

    def procesar_ejercicio(self):
        try:
            a = float(self.txt_a.text())
            b = float(self.txt_b.text())
            x = float(self.txt_x.text())
            
            calculadora = Distribucion(a, b, x)
            resultado = calculadora.calcular_fx()
            
            self.lbl_resultado.setText(f"Resultado de fx: {resultado:.6f}")
            
        except ValueError:
            self.lbl_resultado.setText("Por favor, ingresa valores numéricos válidos.")