class AsignadorGrupos:
    def __init__(self, nombre, sexo):
        self.nombre = nombre.lower()
        self.sexo = sexo.upper()

    def determinar_grupo(self):
        if self.sexo == "F":
            if self.nombre < "m":
                return "A"
            else:
                return "B"
        else:
            if self.nombre > "n":
                return "A"
            else:
                return "B"
