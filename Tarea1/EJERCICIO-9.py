
class Numeros:
    def __init__(self):
        pass

    def evaluar(self):
        num = int(input('Ingrese numero entero: '))
        V = int(input('Ingrese valor'))
        if num == 1:
            print('Respuesta: ', 100*V)
        elif num == 2:
            print('Respuesta: ',100**V)
        elif num == 3:
            print('Respuesta: ', 100/V)
        else:
            print('Respuesta: ', 0)


valu = Numeros()
valu.evaluar()

