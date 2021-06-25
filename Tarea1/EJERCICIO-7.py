
class Trabajador:
    def __init__(self):
        pass

    def mostrar(self):
        horast = int(input('Ingrese numero de horas trabajadas: '))
        pagoH = float(input('Ingrese pago normal por hora: '))
        if horast > 40:
            horasextras = horast - 40
            if horasextras > 8:
                hextras8 = horasextras - 8
                phe = pagoH * 2 * 8 + pagoH * 3 * hextras8
            else:
                phe = pagoH * 2 * horasextras
            total = pagoH * 40 + phe
        else:
            total= pagoH*horast
        print('Pago total extras trabajadas: ', total)


pago = Trabajador()
pago.mostrar()

