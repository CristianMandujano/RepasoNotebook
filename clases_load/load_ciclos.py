from PyQt5.QtWidgets import QDialog
from PyQt5 import uic

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

class DialogoEjercicio5(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/dialogo_ejercicio5.ui", self)
        
        self.btn_calcular.clicked.connect(self.procesar_ejercicio)

    def procesar_ejercicio(self):
        try:
            valor_n = int(self.txt_input_n.text())
            
            ejercicio = Sumatoria(n=valor_n)
            
            resultado_final = ejercicio.calcular_sumatoria()
            
            self.lbl_resultado.setText(f"Resultado de la sumatoria: {resultado_final:.6f}")
            
        except ValueError:
            self.lbl_resultado.setText("Por favor, ingresa un número entero válido.")

class DialogoEjercicio6(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/dialogo_ejercicio6.ui", self)
        
        self.btn_calcular.clicked.connect(self.procesar_ejercicio)

    def procesar_ejercicio(self):
        try:
            valor_n = int(self.txt_input_n.text())
            
            ejercicio = SumatoriaGeometrica(n=valor_n)
            
            resultado_final = ejercicio.calcular_sumatoria()
            
            self.lbl_resultado.setText(f"Resultado de la serie: {resultado_final:.6f}")
            
        except ValueError:
            self.lbl_resultado.setText("Por favor, ingresa un número entero válido.")

class DialogoEjercicio7(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/dialogo_ejercicio7.ui", self)
        
        self.btn_calcular.clicked.connect(self.procesar_ejercicio)

    def procesar_ejercicio(self):
        try:
            numero = int(self.txt_input_numero.text())
            
            ejercicio = TablaMultiplicar(numero=numero)
            
            tabla_resultado = ejercicio.generar_tabla()
            
            resultado_formateado = "\n".join([f"{numero} x {i} = {resultado}" for i, resultado in enumerate(tabla_resultado, start=1)])
            
            self.lbl_resultado.setText(resultado_formateado)
            
        except ValueError:
            self.lbl_resultado.setText("Por favor, ingresa un número entero válido.")

class DialogoEjercicio8(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/dialogo_ejercicio8.ui", self)
        
        self.btn_calcular.clicked.connect(self.procesar_ejercicio)

    def procesar_ejercicio(self):
        try:
            numero = int(self.txt_input_numero.text())
            
            ejercicio = TablaMultiplicar1_10(numero=numero)
            
            tabla_resultado = ejercicio.generar_tabla()
            
            resultado_formateado = "\n".join([f"{numero} x {i} = {resultado}" for i, resultado in enumerate(tabla_resultado, start=1)])
            
            self.lbl_resultado.setText(resultado_formateado)
            
        except ValueError:
            self.lbl_resultado.setText("Por favor, ingresa un número entero válido.")

class DialogoEjercicio9(QDialog):   
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/dialogo_ejercicio9.ui", self)
        
        self.btn_calcular.clicked.connect(self.procesar_ejercicio)

    def procesar_ejercicio(self):
        palabra = self.txt_input_palabra.text()
        
        ejercicio = RepetidorPalabra(palabra=palabra)
        
        resultado = ejercicio.mostrar_diez_veces()
        
        self.lbl_resultado.setText(resultado)

class DialogoEjercicio10(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/dialogo_ejercicio10.ui", self)
        
        self.btn_calcular.clicked.connect(self.procesar_ejercicio)

    def procesar_ejercicio(self):
        try:
            edad = int(self.txt_input_edad.text())
            
            ejercicio = ContadorEdad(edad=edad)
            
            resultado = ejercicio.mostrar_anios_cumplidos()
            
            resultado_formateado = "\n".join([f"Año {i}: {cumplido} años cumplidos" for i, cumplido in enumerate(resultado, start=1)])
            
            self.lbl_resultado.setText(resultado_formateado)
            
        except ValueError:
            self.lbl_resultado.setText("Por favor, ingresa un número entero válido.")

class DialogoEjercicio11(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/dialogo_ejercicio11.ui", self)
        
        self.btn_calcular.clicked.connect(self.procesar_ejercicio)

    def procesar_ejercicio(self):
        try:
            numero = int(self.txt_input_numero.text())
            
            ejercicio = ImparesConsecutivos(numero=numero)
            
            resultado = ejercicio.mostrar_impares()
            
            self.lbl_resultado.setText(resultado)
            
        except ValueError:
            self.lbl_resultado.setText("Por favor, ingresa un número entero válido.")

class DialogoEjercicio12(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/dialogo_ejercicio12.ui", self)
        
        self.btn_calcular.clicked.connect(self.procesar_ejercicio)

    def procesar_ejercicio(self):
        try:
            numero = int(self.txt_input_numero.text())
            
            ejercicio = CuentaAtras(numero=numero)
            
            resultado = ejercicio.generar_cuenta()
            
            resultado_formateado = "\n".join([f"{i}" for i in resultado])
            
            self.lbl_resultado.setText(resultado_formateado)
            
        except ValueError:
            self.lbl_resultado.setText("Por favor, ingresa un número entero válido.")

class DialogoEjercicio13(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/dialogo_ejercicio13.ui", self)
        
        self.btn_calcular.clicked.connect(self.procesar_ejercicio)

    def procesar_ejercicio(self):
        try:
            capital_inicial = float(self.txt_input_capital.text())
            tasa_interes = float(self.txt_input_tasa.text())
            anios = int(self.txt_input_anios.text())
            
            ejercicio = CalculadoraInversion(capital_inicial=capital_inicial, tasa_interes=tasa_interes, anios=anios)
            
            resultado = ejercicio.calcular_rendimientos()
            
            resultado_formateado = "\n".join([f"Año {i}: Capital acumulado = {capital:.2f}" for i, capital in enumerate(resultado, start=1)])
            
            self.lbl_resultado.setText(resultado_formateado)
            
        except ValueError:
            self.lbl_resultado.setText("Por favor, ingresa valores numéricos válidos.")

class DialogoEjercicio15(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/dialogo_ejercicio15.ui", self)
        
        self.btn_calcular.clicked.connect(self.procesar_ejercicio)

    def procesar_ejercicio(self):
        frase = self.txt_input_frase.text()
        
        ejercicio = PalabraInversa(frase=frase)
        
        resultado = ejercicio.mostrar_al_reves()
        
        self.lbl_resultado.setText(resultado)

class DialogoEjercicio16(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/dialogo_ejercicio16.ui", self)
        
        self.btn_calcular.clicked.connect(self.procesar_ejercicio)

    def procesar_ejercicio(self):
        frase = self.txt_input_frase.text()
        
        ejercicio = ContadorLetras(frase=frase)
        
        resultado = ejercicio.contar()
        
        resultado_formateado = "\n".join([f"Letra '{letra}': {conteo} veces" for letra, conteo in resultado.items()])
        
        self.lbl_resultado.setText(resultado_formateado)

class DialogoEjercicio19(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/dialogo_ejercicio19.ui", self)
        
        self.btn_calcular.clicked.connect(self.procesar_ejercicio)

    def procesar_ejercicio(self):
        nombre = self.txt_input_nombre.text()
        
        ejercicio = Saludador(nombre=nombre)
        
        resultado = ejercicio.dar_bienvenida()
        
        self.lbl_resultado.setText(resultado)   

class DialogoEjercicio21(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/dialogo_ejercicio21.ui", self)
        
        self.btn_calcular.clicked.connect(self.procesar_ejercicio)

    def procesar_ejercicio(self):
        try:
            num1 = float(self.txt_input_num1.text())
            num2 = float(self.txt_input_num2.text())
            
            ejercicio = Division(num1=num1, num2=num2)
            
            resultado = ejercicio.imprimir_resultado()
            
            self.lbl_resultado.setText(resultado)
            
        except ValueError:
            self.lbl_resultado.setText("Por favor, ingresa valores numéricos válidos.")

class DialogoEjercicio22(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/dialogo_ejercicio22.ui", self)
        
        self.btn_calcular.clicked.connect(self.procesar_ejercicio)

    def procesar_ejercicio(self):
        try:
            capital_inicial = float(self.txt_input_capital.text())
            tasa_interes = float(self.txt_input_tasa.text())
            anios = int(self.txt_input_anios.text())
            
            ejercicio = CuentaAhorros(capital_inicial=capital_inicial, tasa_interes=tasa_interes, anios=anios)
            
            resultado = ejercicio.calcular_rendimientos()
            
            resultado_formateado = "\n".join([f"Año {i}: Capital acumulado = {capital:.2f}" for i, capital in enumerate(resultado, start=1)])
            
            self.lbl_resultado.setText(resultado_formateado)
            
        except ValueError:
            self.lbl_resultado.setText("Por favor, ingresa valores numéricos válidos.")

class DialogoEjercicio23(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/dialogo_ejercicio23.ui", self)
        
        self.btn_calcular.clicked.connect(self.procesar_ejercicio)

    def procesar_ejercicio(self):
        try:
            precio_pan = float(self.txt_input_precio.text())
            cantidad_pan = int(self.txt_input_cantidad.text())
            
            ejercicio = CalculadoraPan(precio_pan=precio_pan, cantidad_pan=cantidad_pan)
            
            resultado = ejercicio.calcular_total()
            
            self.lbl_resultado.setText(f"El costo total del pan es: {resultado:.2f}€")
            
        except ValueError:
            self.lbl_resultado.setText("Por favor, ingresa valores numéricos válidos.")

class DialogoEjercicio25(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/dialogo_ejercicio25.ui", self)
        
        self.btn_calcular.clicked.connect(self.procesar_ejercicio)

    def procesar_ejercicio(self):
        frase = self.txt_input_frase.text()
        
        ejercicio = InversorFrase(frase=frase)
        
        resultado = ejercicio.invertir_palabras()
        
        self.lbl_resultado.setText(resultado)

