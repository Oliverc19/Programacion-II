import random

# Clase base
class Juego:
    def __init__(self, vidas):
        self.numeroDeVidas = vidas
        self.record = 0

    def reiniciaPartida(self):
        print("\n--- Nueva partida ---")

    def actualizaRecord(self):
        self.record += 1
        print("Record:", self.record)

    def quitaVida(self):
        self.numeroDeVidas -= 1
        print("Vidas restantes:", self.numeroDeVidas)

        if self.numeroDeVidas > 0:
            return True
        else:
            print("Sin vidas")
            return False
# Clase intermedia
class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas):
        super().__init__(vidas)
        self.numeroAAdivinar = 0

    def validaNumero(self, n):
        if 0 <= n <= 10:
            return True
        else:
            print("Número fuera de rango (0-10)")
            return False

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)

        while True:
            intento = int(input("Ingresa un número (0-10): "))

            # validar
            if not self.validaNumero(intento):
                continue

            if intento == self.numeroAAdivinar:
                print("¡Acertaste!")
                self.actualizaRecord()
                break
            else:
                if not self.quitaVida():
                    print("El número era:", self.numeroAAdivinar)
                    break

                if intento < self.numeroAAdivinar:
                    print("Es mayor")
                else:
                    print("Es menor")
# Juego PAR
class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, n):
        if not (0 <= n <= 10):
            print("Número fuera de rango")
            return False
        if n % 2 != 0:
            print("Error: el número debe ser PAR")
            return False
        return True
# Juego IMPAR
class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, n):
        if not (0 <= n <= 10):
            print("Número fuera de rango")
            return False
        if n % 2 == 0:
            print("Error: el número debe ser IMPAR")
            return False
        return True
# Aplicación
class Aplicacion:
    @staticmethod
    def main():
        print("Juego normal")
        juego1 = JuegoAdivinaNumero(3)
        juego1.juega()

        print("\nJuego de números PARES")
        juego2 = JuegoAdivinaPar(3)
        juego2.juega()

        print("\nJuego de números IMPARES")
        juego3 = JuegoAdivinaImpar(3)
        juego3.juega()
# Ejecutar
Aplicacion.main()