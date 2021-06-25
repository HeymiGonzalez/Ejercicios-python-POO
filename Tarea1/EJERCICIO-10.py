
class Aspirante:
    def __init__(self):
        pass

    def usoAND(self):
        califcacion1 = float(input('Ingrese calificacion 1: '))
        calificacion2 = float(input('Ingrese calificacion 2: '))
        if (califcacion1 >= 80) and (calificacion2 >= 80):
            print('Aceptado')
        else:
            print('Rechazado')

    def usoOR(self):
        calificacion1 = float(input('Ingrese calificacion 1: '))
        calificacion2 = float(input('Ingrese calificacion 2: '))
        if (calificacion1 >= 80) or (calificacion2 >= 80):
            print('Aceptado')
        else:
            print('Rechazado')

prueba = Aspirante()
prueba.usoAND()
prueba.usoOR()