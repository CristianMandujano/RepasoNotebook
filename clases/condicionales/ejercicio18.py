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

nom = input("¿Cuál es tu nombre? ")
sex = input("¿Cuál es tu sexo (M o F)? ")

sistema = AsignadorGrupos(nom, sex)
grupo_final = sistema.determinar_grupo()

print(f"Tu grupo es {grupo_final}")