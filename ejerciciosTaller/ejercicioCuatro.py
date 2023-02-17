# 4. Cree una clase Rectángulo la cual contiene dos atributos de instancia que representan los puntos que definen sus esquinas.
# Agregue métodos a la clase Rectángulo para calcular su perímetro, calcular su área e indicar si el rectángulo es un cuadrado.

from ejercicioDos import Punto


class Rectangulo:
    def __init__(self, punto_1: Punto, punto_2: Punto):

        self.punto_1 = punto_1
        self.punto_2 = punto_2

        self.base = self.punto_2.x - self.punto_1.x
        self.altura = self.punto_2.y - self.punto_1.y

    def calcular_perimetro(self) -> float:

        perimetro = 2 * self.base + 2 * self.altura
        return perimetro

    def calcular_area(self) -> float:

        area = self.base * self.altura
        return area

    def si_es_cuadrado(self):

        if self.base == self.altura:
            print("Si es un cuadrado")
        else:
            print("No es un cuadrado")
