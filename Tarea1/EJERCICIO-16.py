
class Arreglos:
    def __init__(self):
        pass

    def arreglo1(self):
        nuevo_vector = []
        A = []
        B = []
        for j in range(0,20):
            numero = int(input('Ingrese numero: '))
            nuevo_vector.append(numero)
        for j in nuevo_vector:
            if j >= 0:
                B.append(j)
            else:
                A.append(j)
        print('Vector A con numeros negativos: {}'.format(A))
        print('Vector B con numeros positivos: {}'.format(B))


mostrar = Arreglos()
mostrar.arreglo1()

