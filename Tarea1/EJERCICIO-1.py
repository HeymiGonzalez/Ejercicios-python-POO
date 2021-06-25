
class Superficie:
    def __init__(self):
        pass

    def mostrarSuperficie(self):
        radio = float(input('Ingrese radio: '))
        pi = 3.1416
        respuesta = pi*(radio**2)
        print('Superficie del circulo = {}'.format(respuesta))


resul = Superficie()
resul.mostrarSuperficie()

