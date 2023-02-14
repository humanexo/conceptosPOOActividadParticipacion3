# 2. Cree una clase Punto que represente un punto en el plano cartesiano.

class Punto:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def mostrarPunto(self):
        print(f"{self.x}, X, {self.y} Y")


    def moverpunto(self, nuevaX : int, nuevaY : int ):
        self.x = nuevaX
        self.y = nuevaY

    def calculardistancia(self, otropunto):
        distanciaenx = self.x - otropunto.x
        distanciaeny = self.y - otropunto.y


    def __init__(self, coordenadasPunto):
        self.coordenadas_del_Punto: Punto = coordenadasPunto


