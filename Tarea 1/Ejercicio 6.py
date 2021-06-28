
class Empleado:
    def __init__(self):
        pass

    # Ejercicio 6 :
    def Sueldo(self):
        s = float(input('Ingrese sueldo: '))
        if s < 600:
            nuevoS = s + s*0.10
            print('Su sueldo mas el 10% es: ${}.'.format(nuevoS))
        else:
            sueldo = s
            print('Usted no recibe aumento. Su sueldo es: $', sueldo)


sueld = Empleado()
sueld.Sueldo()