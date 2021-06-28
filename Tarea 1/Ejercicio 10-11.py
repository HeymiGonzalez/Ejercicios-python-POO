
class Aspirante:
    def __init__(self):
        pass

    # Ejercicio 10
    def usoAND(self):
        califcacion1 = float(input('Ingrese calificacion 1: '))
        calificacion2 = float(input('Ingrese calificacion 2: '))
        if (califcacion1 > 80) and (calificacion2 > 80):
            print('Aceptado')
        else:
            print('Rechazado')

    # Ejercicio 11
    def usoOR(self):
        calificacion1 = float(input('Ingrese calificacion 1: '))
        calificacion2 = float(input('Ingrese calificacion 2: '))
        if (calificacion1 > 90) or (calificacion2 > 90):
            print('Aceptado')
        else:
            print('Rechazado')

prueba = Aspirante()
prueba.usoAND()
prueba.usoOR()