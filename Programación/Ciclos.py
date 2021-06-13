
class Ciclo:
    def __init__(self, n1=5): # Metodo constructor que inicializa los atributos de la clase.
        self.number1 = n1  # Variable de instancia

    def utilidadWhile(self):
        caracter = input('Ingrese una vocal: ').lower()
        while caracter not in ('a','e','i','o','u'):
            caracter = input('Ingrese una vocal: ').lower()
        print('Correcto. Ha ingresado una vocal')


ciclo1 = Ciclo()
ciclo1.utilidadWhile()
