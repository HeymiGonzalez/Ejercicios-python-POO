
class Datos:
    inst = 0  # Variable de clase
    def __init__(self, dato ='Inicio'):  #Metodo constructor
        self.mensaje = dato # Variable de instancia

    def Detalles(self):
        nombres = 'Heymi Gonzalez'
        edad, peso = 18, 60
        sexo = 'F'
        civil = True
        # tuplas, colecciones inmutables
        usuario = ()
        usuario = ('heymi', 1234, 'heymi@gmail.com', True)
        # usuario[3] = 'Milagro'
        # listas, colecciones mutables
        materias = []
        materias = ['Programacion', 'Redes', 'Diseño']
        materias[1] = 'Python'
        materias.append('Administracion')
        # Diccionarios, colecciones de objetos clave:valor
        docente = {}
        docente = {'nombre':'Daniel', 'edad':50, 'fac':'faci'}
        docente['carrera'] = 'cs'
        # presentacion usando format
        print('NOMBRES:{}, EDAD:{}, PESO:{}, SEXO:{}, CIVIL:{}'.format(nombres, edad, peso, sexo, civil))
        # print(usuario, materias, docente)
        # print(usuario,usuario[0], usuario[0:2],usuario[-1])
        # print(materias,materias[2:],materias[:1],materias[::],materias[-2:])
        # print(docente,docente['nombre'])



info = Datos()  # Se crea el objeto, instancia de la clase
info.Detalles()  # Llamada a un metodo de la clase
# print(info.mensaje)  # Llamada a un atributo de la clase


