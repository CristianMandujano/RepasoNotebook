class Saludador:
    def __init__(self, nombre):
        self.nombre = nombre

    def dar_bienvenida(self):
        return f"¡Hola {self.nombre}!"

nombre_usuario = input("¿Cuál es tu nombre? ")

usuario = Saludador(nombre_usuario)
mensaje = usuario.dar_bienvenida()

print(mensaje)