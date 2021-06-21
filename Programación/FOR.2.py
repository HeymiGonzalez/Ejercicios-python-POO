
# CLASE SEMANA3, Jueves 17-Junio-2021.

class For:
    def __init__(self):
        pass

    def utilidadFor(self):
        detalles = ["Daniel", 50, True]
        num = (2, 4.8, 6, 8)
        docente = {'nombre':'Daniel', 'edad':50, 'facultad':'faci'}
        lnotas = [(20,30), (40,50), (60,70)]
        lAlumnos = [{'nombre': 'Erick', 'notafinal': 70}, {'nombre': 'Yady', 'notafinal': 60}, {'nombre': 'Daniel', 'notafinal': 80}]

        acumulador=0
        contador=0
        for notas in lnotas:
            #print(notas)
            sumParcial=0
            for nota in notas:
               #print(nota)
               contador+=1
               acumulador+=nota
               sumParcial+=nota
            promParcial = sumParcial/len(notas)
            print('Notas parciales={} - Promedio parciaL={}'.format(notas,promParcial))
        prom = acumulador/contador
        print('Suma notas = {} -- Numero Notas = {} -- Promedio General = {}'.format(acumulador, contador, prom))

        # acum=0
        # con=0
        # for alumnos in lAlumnos:
        #     print(alumnos)
        #     for c,v in alumnos.items():
        #         print(c,':',v)
        #         if c=='notafinal': acum+=v
        #     con+=1
        # print('Suma Notas={} - Cantidad Notas={} - NotaFinal={}'.format(acum,con, acum/con))


ciclo = For()
ciclo.utilidadFor()
