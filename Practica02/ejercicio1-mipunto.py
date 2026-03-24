

import math  
class MiPunto:
    def __init__(self, x=0, y=0):
        self.__x = x  
        self.__y = y   

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

   
    def distancia(self, otro_punto_o_x, y=None):

        if isinstance(otro_punto_o_x, MiPunto):
            
            dx = self.__x - otro_punto_o_x.getX()
            dy = self.__y - otro_punto_o_x.getY()
        else:
           
            dx = self.__x - otro_punto_o_x
            dy = self.__y - y

        return math.sqrt(dx**2 + dy**2)

    def __str__(self):
        return f"({self.__x}, {self.__y})"


if __name__ == "__main__":
    p1 = MiPunto(0, 0)
    p2 = MiPunto(10, 30.5)

    print("=== Ejercicio 1: Clase MiPunto ===")
    print(f"Punto 1: {p1}")
    print(f"Punto 2: {p2}")

    dist1 = p1.distancia(p2)
    print(f"\nDistancia entre {p1} y {p2} (usando objeto): {dist1:.4f}")

    dist2 = p1.distancia(10, 30.5)
    print(f"Distancia entre {p1} y (10, 30.5) (usando coords): {dist2:.4f}")
