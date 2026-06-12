import sys
from PyQt5.QtWidgets import QApplication
from clases_load.load_ventana_principal import VentanaPrincipal

if __name__ == "__main__":
    # 1. Creamos la aplicación de Qt
    app = QApplication(sys.argv)
    
    # 2. Instanciamos tu ventana principal
    menu = VentanaPrincipal()
    
    # 3. La mostramos en pantalla
    menu.show()
    
    # 4. Cerramos el proceso limpiamente al salir
    sys.exit(app.exec_())