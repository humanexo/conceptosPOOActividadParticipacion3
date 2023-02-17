# 2. Cree una clase Punto que represente un punto en el plano cartesiano.

class Punto:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y


    # 3. A la clase del punto anterior, defínale los siguientes métodos:
    # - Un método mostrar que imprima por consola las coordenadas del punto
    # - Un método mover que cambie las coordenadas del punto
    # - Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto.


    def mostrarPunto(self):
        print(f"{self.x}, X, {self.y} Y")

    def moverpunto(self, nuevaX: int, nuevaY: int):
        self.x = nuevaX
        self.y = nuevaY

    def calculardistancia(self, otropunto):
        distanciaenx = self.x-otropunto.x
        distanciaeny =self.y-otropunto.y
        print(distanciaenx, distanciaeny)



