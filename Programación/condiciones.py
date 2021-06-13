
class Condicion:
    con = 0   # Variable de clase
    def __init__(self, n1=0,n2=1): #Metodo constructor que inicializa los atributos de la clase.
        self.number1 = n1  # Variable de instancia
        self.number2 = n2  # Variable de instancia

        self.number3 = n1  # Variable de instancia

    def utilizacionIf(self):
        if self.number1 == self.number2:
            print('Los numeros: n1={} y n2={}, son iguales'.format(self.number1,self.number2))
        elif self.number1 == self.number3:
            print('Los numeros: n1={} y n3={} , son iguales'.format(self.number1,self.number3))
        else:
            print("Los numeros no son iguales")


# c1 = Condicion() # Creamos un objeto, instancia de la clase
# print(c1.number1)
# print(c1.number2)

c2 = Condicion(10,20)
c2.utilizacionIf()  # Llamada a un metodo de la clase
#print(c2.number1)  # Llamada a un atributo de la clase