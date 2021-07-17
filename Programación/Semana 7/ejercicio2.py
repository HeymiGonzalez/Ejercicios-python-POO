
class Persona:
    _siguiente = 0

    def __init__(self, nombre='Invitado',activo=True):
        self.__codigo = self.siguiente()
        self.__nombre = self.__nombreMayuscula(nombre)
        self.activo = activo

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nom):
        self.__nombre = nom
    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, cod):
        self.__codigo = cod

    def siguiente(self):
        Persona._siguiente = Persona._siguiente+1
        return Persona._siguiente

    def __nombreMayuscula(self, nomb):
        return nomb.upper()

    def mostrar(self):
        return 'Codigo: {} - Nombre: {} - Activo: {}'.format(self.codigo, self.nombre, self.activo)


class empleado(Persona):
    def __init__(self, nom='Invitado',acti=True, sueldo=500):
        Persona.__init__(self,nom,acti)
        self.sueldo = sueldo


pers1 = Persona()
print(pers1.mostrar())
pers2 = Persona('Heymi', False)
print(pers2.mostrar())
