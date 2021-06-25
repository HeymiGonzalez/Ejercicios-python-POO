
class Numeros:
    def __init__(self):
        pass

    def Identificar(self):
        num1 = float(input('Ingrese primer numero: '))
        num2 = float(input('Ingrese segundo numero: '))
        num3 = float(input('Ingrese tercer numero: '))
        if (num1>num2) and (num1>num3):
            print('El numero mayor es: ', num1)
        elif (num2>num1) and (num2>num3):
            print('El numero mayor es: ', num2)
        else:
            print('El numero mayor es: ', num3)


iden = Numeros()
iden.Identificar()