
class Bucle:
    def __init__(self):
        pass

    # Ejercicio 17
    def bucle_repeat(self):
        serie = 0
        i = 1
        numero = int(input('Ingrese numero: '))
        band = True
        while band:
            if band == True:
                serie = serie + (1/i)
                band = False
            else:
                serie = serie - (1/i)
                band = True
            i += 1
            if i > numero:
                break
            print('Resultado de la serie ', serie)

    # Ejercicio 18
    def bucle_anidado(self):
        numero = int(input('Ingrese numero: '))
        factorial = 1
        for i in range(1, numero+1):
            factorial *= i
        print('El factorial del numero {} es: {} '.format(numero, factorial))


calculo = Bucle()
calculo.bucle_repeat()
calculo.bucle_anidado()

