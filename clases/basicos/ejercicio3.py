import math

class Distribucion:
    def __init__(self, x, m, s):
        self.x = x
        self.m = m
        self.s = s

    def calcular_fx(self):
        resultado = 1 / math.sqrt(2 * math.pi * self.s) * math.e ** (1/2 * ((self.x - self.m) / self.s) ** 2)
        return resultado
