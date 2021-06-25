
class Compra:
    def __init__(self):
        pass

    def calculoPago(self):
        compra = float(input('Ingrese el valor de la compra: '))
        desc = compra*0.15
        totalPagar = compra-desc
        print('El total a pagar es: ${} dólares.'.format(totalPagar))


pagar = Compra()
pagar.calculoPago()