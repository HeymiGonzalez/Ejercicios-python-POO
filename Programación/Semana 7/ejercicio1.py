
class Ordenar:
    def __init__(self, lista):
        self.lista = lista
    def borbuja(self):
        for i in range(len(self.lista)):
            for j in range(i+1, len(self.lista)):
                if self.lista[i] > self.lista[j]:
                    a = self.lista[i]
                    self.lista[i] = self.lista[j]
                    self.lista[j] = a
    def insertar(self,dato):
        self.borbuja()
        nuelista=[]
        band = False
        for pos,elemento in enumerate(self.lista):
            if elemento > dato:
                nuelista.append(dato)
                band = True
                break
        if band == True:
            self.lista = self.lista[0:pos] + nuelista + self.lista[pos:]
        else:
            self.lista.append(dato)
        return self.lista

    def insertar2(self,dato):
        self.lista.sort()
        self.borbuja()
        nuelista=[]
        band = False
        for pos,elemento in enumerate(self.lista):
            if elemento > dato:
                band = True
                break
        if band:
            for i in range(pos):
                nuelista.append(self.lista[i])
            nuelista.append(dato)
            for j in range(pos,len(self.lista)):
                nuelista.append(self.lista[j])
            self.lista = nuelista
        else:
            self.lista.append(dato)
        return self.lista


orden = Ordenar([10,15,20,70,80])
#print(orden.insertar(90))
print(orden.insertar2(50))
# orden.borbuja()
# print(orden.lista)