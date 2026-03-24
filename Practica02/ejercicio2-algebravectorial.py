import math


class AlgebraVectorial:
    def __init__(self, a1=0, a2=0, a3=0):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    def longitud(self):
        return math.sqrt(self.a1**2 + self.a2**2 + self.a3**2)
    def _dot(self, b):
        return self.a1*b.a1 + self.a2*b.a2 + self.a3*b.a3
    def _cross(self, b):
        c1 = self.a2*b.a3 - self.a3*b.a2
        c2 = self.a3*b.a1 - self.a1*b.a3
        c3 = self.a1*b.a2 - self.a2*b.a1
        return AlgebraVectorial(c1, c2, c3)
# inciso A
    def perpendicular_diagonales(self, b):
        suma = AlgebraVectorial(self.a1+b.a1, self.a2+b.a2, self.a3+b.a3)
        resta = AlgebraVectorial(self.a1-b.a1, self.a2-b.a2, self.a3-b.a3)
        return math.isclose(suma.longitud(), resta.longitud(), rel_tol=1e-9)
#INCISO B
    def perpendicular_mutua(self, b):
        ab = AlgebraVectorial(self.a1-b.a1, self.a2-b.a2, self.a3-b.a3)
        ba = AlgebraVectorial(b.a1-self.a1, b.a2-self.a2, b.a3-self.a3)
        return math.isclose(ab.longitud(), ba.longitud(), rel_tol=1e-9)
    # INCISO C
    def perpendicular_dot(self, b):
        return math.isclose(self._dot(b), 0, abs_tol=1e-9)
# INCISO D
    def perpendicular_pitagoras(self, b):
        suma = AlgebraVectorial(self.a1+b.a1, self.a2+b.a2, self.a3+b.a3)
        lado_izq = suma.longitud()**2
        lado_der = self.longitud()**2 + b.longitud()**2
        return math.isclose(lado_izq, lado_der, rel_tol=1e-9)
# INCISO D
    def paralela_escalar(self, b):
        r_values = []
        pares = [(self.a1, b.a1), (self.a2, b.a2), (self.a3, b.a3)]
        for ai, bi in pares:
            if bi != 0:
                r_values.append(ai / bi)
            elif ai != 0:
                return False  
        if not r_values:
            return True  
        return all(math.isclose(r, r_values[0], rel_tol=1e-9) for r in r_values)
# INCISO F
    def paralela_cross(self, b):
        cruz = self._cross(b)
        return math.isclose(cruz.longitud(), 0, abs_tol=1e-9)
# INCISO G
    def proyeccion(self, b):
        if math.isclose(b.longitud(), 0, abs_tol=1e-9):
            raise ValueError("No se puede proyectar sobre el vector cero")
        escalar = self._dot(b) / (b.longitud()**2)
        return AlgebraVectorial(escalar*b.a1, escalar*b.a2, escalar*b.a3)
# INCISO H
    def componente(self, b):
        if math.isclose(b.longitud(), 0, abs_tol=1e-9):
            raise ValueError("No se puede calcular componente sobre vector cero")
        return self._dot(b) / b.longitud()

    def __str__(self):
        return f"({self.a1}, {self.a2}, {self.a3})"
# PROGRAMA PRUEBA
if __name__ == "__main__":
    print("=== Ejercicio 2: AlgebraVectorial ===\n")

    a = AlgebraVectorial(1, 0, 0)
    b = AlgebraVectorial(0, 1, 0)

    print(f"Vector a = {a}")
    print(f"Vector b = {b}")
    print(f"\n-- Perpendiculares --")
    print(f"a) |a+b|==|a-b|        : {a.perpendicular_diagonales(b)}")
    print(f"b) |a-b|==|b-a|        : {a.perpendicular_mutua(b)}")
    print(f"c) a·b == 0            : {a.perpendicular_dot(b)}")
    print(f"d) |a+b|²==|a|²+|b|²  : {a.perpendicular_pitagoras(b)}")
# VECT PARALELOS
    a2 = AlgebraVectorial(2, 4, 6)
    b2 = AlgebraVectorial(1, 2, 3)
    print(f"\nVector a2 = {a2}")
    print(f"Vector b2 = {b2}")
    print(f"\n-- Paralelas --")
    print(f"e) a = r*b             : {a2.paralela_escalar(b2)}")
    print(f"f) a x b == 0          : {a2.paralela_cross(b2)}")
#PROY Y COMPONENTE
    a3 = AlgebraVectorial(3, 4, 0)
    b3 = AlgebraVectorial(1, 0, 0)
    print(f"\nVector a3 = {a3}")
    print(f"Vector b3 = {b3}")
    proy = a3.proyeccion(b3)
    comp = a3.componente(b3)
    print(f"\ng) Proyeccion de a3 sobre b3 : {proy}")
    print(f"h) Componente de a3 en b3    : {comp}")
