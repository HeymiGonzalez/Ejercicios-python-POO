'''Mismo ejercicio, pero ahora usando parametros
y atributo de clase'''

class Cargo:
    secuencia = 0
    def __init__(self, desc='No tiene cargo'):
        Cargo.secuencia = Cargo.secuencia + 1
        self.codigo = Cargo.secuencia
        self.descripcion = desc


if __name__ == '__main__':
    cargo1 = Cargo()
    print(cargo1.codigo, cargo1.descripcion)
    cargo2 = Cargo('Analista')
    print(cargo2.codigo, cargo2.descripcion)
    cargo3 = Cargo()
    cargo3.descripcion = 'Director'
    print(cargo3.codigo, cargo3.descripcion)

    # Se puede llamar al atributo de la clase, sin necesidad de instanciar.
    print(Cargo.secuencia)



