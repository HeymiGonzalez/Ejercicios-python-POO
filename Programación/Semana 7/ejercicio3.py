
class Logica:
    def __init__(self, lista=None):
        self.__lista = lista

    @property
    def lista(self):
        return self.__lista
    @lista.setter
    def lista(self, nue_lista):
        self.__lista = nue_lista

    def par_Impar(self, numero):
        residuo = numero % 2
        if residuo == 0:
            print('El número {} es par'.format(numero))
        else:
            print('El número {} es impar'.format(numero))

    def perfecto(self, numero):
        acu = 0
        for cont in range(1,numero):
            resi = numero % cont
            if resi == 0:
                acu += cont
        if acu == num:
            print('El numero {} es perfecto'.format(numero))
        else:
            print('El numero {} no es perfecto'.format(numero))


class Ejercicio(Logica):
    def __init__(self, lista, numeros):
        super().__init__(lista)
        self.info = numeros

    def suma(self, n1,n2,n3):
        return n1 + n2 + n3

    def par_Impar(self, numero):
        super().par_Impar(numero)
        return numero % 2


log = Logica([2,5,6])
print('\nPRESENTACION DEL CONSTRUCTOR DE LOGICA')
log.lista=[4,7]
print(log.lista)

log1 = Logica()
print('\nPRESENTACION DE METODO PAR E IMPAR')
num = int(input('Ingrese numero: '))
log1.par_Impar(num)
print('\nPRESENTACION DE METODO PERFECTO')
log1.perfecto(6)

log2 = Ejercicio([4,7,8],9)
print('\nPRESENTACION DE CLASS EJERCICIO')
if log2.par_Impar(6) == 0:
    print('Numero par')
else:
    print('Numero impar')
print(log2.suma(6,8,5))
print(log2.lista)