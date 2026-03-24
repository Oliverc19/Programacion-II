import math


class Vector3D:
    def __init__(self, a1=0, a2=0, a3=0):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
# A)
    def __add__(self, b):
        return Vector3D(self.a1 + b.a1,
                        self.a2 + b.a2,
                        self.a3 + b.a3)

    def __sub__(self, b):
        return Vector3D(self.a1 - b.a1,
                        self.a2 - b.a2,
                        self.a3 - b.a3)
# B)
    def __mul__(self, r):
        if isinstance(r, (int, float)):
            return Vector3D(r * self.a1, r * self.a2, r * self.a3)
        raise TypeError("Solo se puede multiplicar por un escalar (int o float)")

    def __rmul__(self, r):
        return self.__mul__(r)
# C)
    def longitud(self):
        return math.sqrt(self.a1**2 + self.a2**2 + self.a3**2)

    def __abs__(self):
        return self.longitud()
# D)
    def normal(self):
        mag = self.longitud()
        if math.isclose(mag, 0, abs_tol=1e-9):
            raise ValueError("No se puede normalizar el vector cero")
        return Vector3D(self.a1 / mag, self.a2 / mag, self.a3 / mag)

# E)
    def __matmul__(self, b):
        return self.a1*b.a1 + self.a2*b.a2 + self.a3*b.a3
# F)
    def __xor__(self, b):
        c1 = self.a2*b.a3 - self.a3*b.a2
        c2 = self.a3*b.a1 - self.a1*b.a3
        c3 = self.a1*b.a2 - self.a2*b.a1
        return Vector3D(c1, c2, c3)

# COMPARAR IGUALDA
    def __eq__(self, b):
        if not isinstance(b, Vector3D):
            return False
        return (math.isclose(self.a1, b.a1, abs_tol=1e-9) and
                math.isclose(self.a2, b.a2, abs_tol=1e-9) and
                math.isclose(self.a3, b.a3, abs_tol=1e-9))

    def __str__(self):
        return f"({round(self.a1,4)}, {round(self.a2,4)}, {round(self.a3,4)})"

    def __repr__(self):
        return self.__str__()


#Programa de prueba 
if __name__ == "__main__":
    print("=== Ejercicio 3: Vector3D con sobrecarga de operadores ===\n")

    a = Vector3D(1, 2, 3)
    b = Vector3D(4, 5, 6)
    r = 3

    print(f"a = {a}")
    print(f"b = {b}")
    print(f"r = {r}")

    # a) Suma
    print(f"\na) a + b               = {a + b}")

    # b) Multiplicacion escalar
    print(f"b) r * a               = {r * a}")
    print(f"   a * r               = {a * r}")

    # c) Longitud
    print(f"c) |a|                 = {abs(a):.4f}")
    print(f"   |b|                 = {abs(b):.4f}")

    # d) Normal
    print(f"d) normal(a)           = {a.normal()}")

    # e) Producto escalar con @
    print(f"e) a · b (a @ b)       = {a @ b}")

    # f) Producto vectorial con ^
    print(f"f) a x b (a ^ b)       = {a ^ b}")

    print("\n--- Verificacion de propiedades ---")

    a2 = Vector3D(1, 0, 0)
    b2 = Vector3D(0, 1, 0)
    print(f"a2={a2}, b2={b2}")
    print(f"  Son perpendiculares (a2·b2==0): {math.isclose(a2 @ b2, 0, abs_tol=1e-9)}")


    a3 = Vector3D(2, 4, 6)
    b3 = Vector3D(1, 2, 3)
    print(f"a3={a3}, b3={b3}")
    cruz = a3 ^ b3
    print(f"  Son paralelos (a3 x b3 == 0): {cruz == Vector3D(0,0,0)}")
