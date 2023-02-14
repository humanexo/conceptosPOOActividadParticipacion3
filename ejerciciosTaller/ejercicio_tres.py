

# 3. A la clase del punto anterior, defínale los siguientes métodos:
# - Un método mostrar que imprima por consola las coordenadas del punto
# - Un método mover que cambie las coordenadas del punto
# - Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto.

if __name__ == "__main__":
    from ejercicioDos import Punto

    Punto1 = Punto(10,8)
    Punto1.mostrarPunto()

    Punto1.moverpunto(6,9)



    Punto2 = Punto(11,5)
    Punto2.mostrarPunto()
    Punto2.calculardistancia(Punto1)


