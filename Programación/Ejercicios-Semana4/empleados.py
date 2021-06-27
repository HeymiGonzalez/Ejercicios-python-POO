
from cargo1 import Cargo

class Empleado:
    secuencia = 0
    def __init__(self, nom,ced, suel, carg):
        self.codigo = self.generar()
        self.nombre = nom
        self.cedula = ced
        self.sueldo = suel
        self.cargo = carg

    def mostrar(self):
        print('Codigo:{}  Nombre:{}   Cargo:{}-{}'.format(self.codigo, self.nombre, self.cargo.codigo, self.cargo.descripcion))

    def generar(self):
        Empleado.secuencia = Empleado.secuencia + 1
        return Empleado.secuencia


cargo1 = Cargo('Docente')
emp = Empleado('Daniel', '120893445', 500, cargo1)
emp.mostrar()
cargo2 = Cargo('Analista')
emp2 = Empleado('Anna', '120563445', 500, cargo2)
emp2.mostrar()
