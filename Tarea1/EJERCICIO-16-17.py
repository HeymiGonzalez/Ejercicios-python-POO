
class Arreglos:
    def __init__(self):
        pass

    def arreglo1(self):            #Ejercicio 16
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
        
    def arreglo2(self):           #Ejercicio 17          
        listaNotas = []
        listaAlumnos = []
        TotalAlumnos = 30
        TotalNotas = 6
        promedioExamen = []

        for alumno in range(1, 31):
            temporalAlum = input('Ingrese nombre de alumno {}: '.format(alumno))
            listaAlumnos.append(temporalAlum)
            for notas in range(1, 7):
                print('La calificación que el alumno "{}" obtuvo en el exámen es: {}'.format(temporalAlum, notas))

                temporalNot = round(float(input('Nota #{}: '.format(notas))), 2)
                if notas == 1:
                    listaNotas.append([temporalNot])
                else:
                    listaNotas[alumno - 1].append(temporalNot)
            print('')


        """Calculo promedio de calificaciones de cada uno de los exámenes."""
        for cantidadExamen in range(6):
            suma_notas = 0
            for nota in listaNotas:
                suma_notas += nota[cantidadExamen]
            promedio = round((suma_notas / TotalAlumnos), 2)
            print('Promedio de exámen {}: {}'.format(cantidadExamen + 1, promedio))

        """Cálculo del promedio de cada alumno."""
        print('')
        for numero, alumno in enumerate(listaAlumnos):
            suma_notas = sum(listaNotas[numero])
            promedio = round((suma_notas / TotalNotas), 2)
            print('{} su promedio es: {}'.format(alumno, promedio))

        """Cálculo del tipo de exámen que tuvo mayor promedio de calificación."""
        prom_mayor = 0
        for numero_examen in range(6):
            suma_notas = 0
            for nota in listaNotas:
                suma_notas += nota[numero_examen]
            promedio = round((suma_notas / TotalAlumnos), 2)
            if prom_mayor < promedio:
                prom_mayor = promedio
            promedioExamen.append(promedio)
        print('')
        print('El exámen', promedioExamen.index(prom_mayor) + 1, 'obtuvo el mayor promedio:', prom_mayor)


mostrar = Arreglos()
mostrar.arreglo1()
mostrar.arreglo2()


