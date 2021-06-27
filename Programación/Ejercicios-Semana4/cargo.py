
'''La clase Cargo() va a contener la 'maqueta'del ejercicio;
mientras que, las instancia de la clase van a otorgar
los valores a los atributos de la clase'''


class Cargo:
    def __init__(self):
        self.codigo = 0
        self.descripcion = ''


cargos1 = Cargo()
cargos1.codigo = 1
cargos1.descripcion = 'Docente'
print(cargos1.codigo, cargos1.descripcion)
cargos2 = Cargo()
cargos2.codigo = 2
cargos2.descripcion = 'Administrador'
print(cargos2.codigo, cargos2.descripcion)