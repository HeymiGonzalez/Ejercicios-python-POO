
class Alumno:
    def __init__(self):
        pass

    # ejercico 4: estructura selectiva simple
    def sentenciaSimple(self):
        calif = float(input('Ingrese calificacion: '))
        if calif >=7:
            print('Usted ha aprobado con nota de:', calif)

    # ejercicio 5. Estructura selectiva doble
    def sentenciaDoble(self):
        calificacion = float(input('Ingrese calificacion: '))
        if calificacion >=7:
            print('Usted ha aprobado con nota de:', calificacion)
        else:
            print('Usted ha reprobado la materia')


alum = Alumno()
alum.sentenciaSimple()
alum.sentenciaDoble()
