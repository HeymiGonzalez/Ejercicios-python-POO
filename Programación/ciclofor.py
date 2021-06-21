
#  CLASE SEMANA3, Martes 14-Junio-2021.

class For:
    def __init__(self):
        pass

    def utilidadFor(self):
        detalles = ["Daniel", 50, True]
        num = (2, 4.8, 6, 8)
        docente = {'nombre':'Daniel', 'edad':50, 'facultad':'faci'}
        lnotas = [(20,30), (30,40), (40,50)]
        lAlumnos = [{'nombre': 'Erick', 'notafinal': 70}, {'nombre': 'Yady', 'notafinal': 60}, {'nombre': 'Daniel', 'notafinal': 80}]

        # Diferentes casos del range
        # for i in range(8):
        #     print('iteracion={}'.format(i),end='  ')
        #
        # for i in range(3,8):
        #     print('iteracion={}'.format(i), end='  ')
        #
        # for i in range(3,9,3):
        #     print('iteracion={}'.format(i), end='  ')

        # for i in range(10,2,-2):
        #     print('iteracion={}'.format(i), end='  ')

        # Aplicaciones del range
        # long = len(detalles)
        # for i in range(long-1,-1,-1):
        #     print(detalles[i])
        #
        # for i, detalle in enumerate(detalles):
        #     print(i, detalle)
        #
        # for detalle in num:
        #     print(detalle)

        # print('\n--Diccionario NOTAS--')
        # for c,v in docente.items():
        #     print(c,':',v)

        for alumnos in lAlumnos:
            for c,v in alumnos.items():
                print(c,':',v)

ciclo = For()
ciclo.utilidadFor()