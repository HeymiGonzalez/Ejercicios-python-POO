
class Operacion:
    def __init__(self, n1, n2):
        self.numero1 = n1
        self.numero2 = n2

    def suma(self):
        suma = self.numero1 + self.numero2
        return suma

    def resta(self):
        if self.numero1 >= self.numero2:
            return self.numero1 - self.numero2
        return 0

    def multiplicacion(self):
        return self.numero1 * self.numero2

    def division(self):
        if self.numero2 != 0: return self.numero1 / self.numero2
        return 0

    def divisionEntera(self):
        if self.numero2 != 0: return self.numero1 // self.numero2
        return 0

    def residuo(self):
        return self.numero1 % self.numero2

    def exponente(self):
        return self.numero1 ** self.numero2

    def mostrar(self):
        print('Operando1={}, Operando2={}'.format(self.numero1, self.numero2))

print('Menu Operaciones Matematicas')
print('1) Suma\n2) Resta\n3) Multiplicacion\n4) Division\n5) Division Entera\n6) Residuo\n7) Exponente\n8) Salir')
opcion = '0'
while opcion != '8':
    opcion = input('Elija opcion [1...8]: ')
    num1 = int(input('Ingrese primer numero: '))
    num2 = int(input('Ingrese segundo numero: '))
    ope = Operacion(num1,num2)
    if opcion == '1':
        print('{} + {} = {}'.format(ope.numero1,ope.numero2,ope.suma()))
    elif opcion == '2':
        print('{} - {} = {}'.format(ope.numero1,ope.numero2,ope.resta()))
    elif opcion == '3':
        print('{} * {} = {}'.format(ope.numero1,ope.numero2,ope.multiplicacion()))
    elif opcion == '4':
        print('{} / {} = {}'.format(ope.numero1,ope.numero2,ope.division()))
    elif opcion == '5':
        print('{} // {} = {}'.format(ope.numero1,ope.numero2,ope.divisionEntera()))
    elif opcion == '6':
        print('{} % {} = {}'.format(ope.numero1,ope.numero2,ope.residuo()))
    elif opcion == '7':
        print('{} ** {} = {}'.format(ope.numero1, ope.numero2, ope.exponente()))

print('GRACIAS POR SU VISITA')