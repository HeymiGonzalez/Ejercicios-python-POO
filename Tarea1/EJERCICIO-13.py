
class SumProduct:
    def __init__(self):
        pass

    def Control_condicicion(self):
        suma = 0
        produc = 1
        resp = input('Desea ingresar (S/N)?: ')
        while(resp != 'N') and (resp != 'n'):
            num = int(input('Ingrese numero: '))
            suma = suma + num
            produc = produc * num
            print('Desea continuar (S/N)?: ')
            resp = input('Ingrese: ')
        print('CONTROLADO POR CONDICION: Total suma: {}  -  Total producto: {}'.format(suma,produc))

    def control_centinela(self):
        suma = 0
        prod = 1
        n = int(input('Ingrese numero: '))
        while n != -1:
            suma = suma + n
            prod = prod * n
            print('CONTROLADO POR CENTINELA: Total suma: {}  -  Total producto: {}'.format(suma,prod))
            n = int(input('Ingrese numero: '))

    def control_banderas(self):
        primo = True
        divisor = 2
        numero = int(input('Ingrese numero: '))
        while (divisor < numero) and (primo == True):
            res = numero % divisor
            if res == 0:
                primo = False
            else:
                divisor += 1
        if primo == True:
            print('Numero {} es primo'.format(numero))
        else:
            print('Numero {} no es primo'.format(numero))



bucles = SumProduct()
bucles.Control_condicicion()
bucles.control_centinela()
bucles.control_banderas()