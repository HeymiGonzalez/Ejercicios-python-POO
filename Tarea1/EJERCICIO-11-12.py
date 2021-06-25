
class Operacion:
    def __init__(self):
        pass

    def cicloFor(self):
        suma=0
        i=1
        for i in range(100):
            suma = suma+i*i
        print('Presentación FOR: Suma de cuadrados de los 100 primeros numeros: ', suma)

    def cicloWhile(self):
        i = 1
        while i <= 100:
            print('Presentación WHILE: ',  i)
            i = i+1


resul = Operacion()
resul.cicloFor()
resul.cicloWhile()



