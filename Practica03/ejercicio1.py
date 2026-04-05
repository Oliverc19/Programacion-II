import random

# Clase padre
class Juego:
    def __init__(self, vidas):
        self.numeroDeVidas = vidas
        self.record = 0

    def reiniciaPartida(self):
        print("Nueva partida iniciada")
    
    def actualizaRecord(self):
        self.record += 1
        print("Record actualizado:", self.record)

    def quitaVida(self):
        self.numeroDeVidas -= 1
        print("Te quedan", self.numeroDeVidas, "vidas")
        
        if self.numeroDeVidas > 0:
            return True
        else:
            print("Ya no tienes vidas")
            return False
# Clase hija
class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas):
        super().__init__(vidas)
        self.numeroAAdivinar = 0

    def juega(self):
        self.reiniciaPartida()

        # número aleatorio entre 0 y 10
        self.numeroAAdivinar = random.randint(0, 10)

        print("Adivina un número entre 0 y 10")

        while True:
            intento = int(input("Ingresa tu número: "))

            if intento == self.numeroAAdivinar:
                print("¡Acertaste!!")
                self.actualizaRecord()
                break
            else:
                sigue = self.quitaVida()

                if not sigue:
                    print("El número era:", self.numeroAAdivinar)
                    break

                if intento < self.numeroAAdivinar:
                    print("El número es MAYOR")
                else:
                    print("El número es MENOR")
# Clase aplicación
class Aplicacion:
    @staticmethod
    def main():
        juego = JuegoAdivinaNumero(3)
        juego.juega()
# Ejecutar
Aplicacion.main()