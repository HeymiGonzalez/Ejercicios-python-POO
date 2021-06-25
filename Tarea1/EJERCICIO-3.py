
class Sueldo:
    def __init__(self):
        pass

    def totales(self):
        base = float(input('Ingrese sueldo base: '))
        venta1 = float(input('Ingrese valor de su primera venta: '))
        venta2 = float(input('Ingrese valor de su segunda venta: '))
        venta3 = float(input('Ingrese valor de su tercera venta: '))
        totalVentas = venta1+venta2+venta3
        comis= totalVentas*0.10
        totalSueldo=base+comis
        print('''Total de ventas obtenidas: ${}     -     Comision del 10%: ${} 
         Por lo tanto, Su Total de sueldo al mes es: {}'''.format(totalVentas,comis,totalSueldo))


suel = Sueldo()
suel.totales()