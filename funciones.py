def cargarDatosEstudiantes(ruta):
    archivo = open(ruta, "r")
    data = archivo.readlines()
    archivo.close()
    estudiantes = {}
    for i in data:
        estudiantes[int(i.split(";")[0])] = i.split(";")[1][:-1]
    return estudiantes

def toFloat(lista):
    for i in range(len(lista)):
        lista[i] = float(lista[i])
    return lista

def cargarDatosCursos(ruta):
    archivo = open(ruta, "r")
    data = archivo.read()
    archivo.close()
    cursos = {}
    data = data.split("\n\n")[:-1]
    for i in data:
        curso = i.split("\n")
        cursos[curso[0].split(";")[0]] = [int(curso[0].split(";")[1]), int(curso[0].split(";")[2])]
        estudiantes = {}
        for j in curso[1:]:
            estudiantes[int(j.split(";")[0])] = toFloat(j.split(";")[1:])
        cursos[curso[0].split(";")[0]].append(estudiantes)
    return cursos

def agregarEstudiante():
    tieneDigitos = True
    while tieneDigitos == True:
        nombre = input("Nombre del estudiante: ")
        tieneDigitos = False
        for i in nombre:
            if i.isdigit():
                tieneDigitos = True
                break
    while True:
        cedula = input("Cédula del estudiante: ")
        try:
            cedula = int(cedula)
            break
        except ValueError:
            pass

    return cedula, nombre

def actualizarEstudiantes(ruta, datos):
    archivo = open(ruta, "w")
    txt = ""
    for i, j in datos.items():
        txt += f"{i};{j}\n"
    archivo.write(txt)

def crearNuevoCurso():
    nombre = input("Nombre del curso: ")
    while True:
        try:
            creditos = int(input("Número de créditos: "))
            break
        except ValueError:
            pass
    while True:
        try:
            notas = int(input("Número de notas: "))
            break
        except ValueError:
            pass
    return nombre, creditos, notas

def actualizarCursos(ruta, datos):
    archivo = open(ruta, "w")
    txt = ""
    for i, j in datos.items():
        txt += f"{i};{j[0]};{j[1]}\n"
        for k, l in j[2].items():
            txt += f"{k};"
            for n in l:
                txt += f"{n};"
            txt = txt[:-1]+"\n"
        txt += "\n"
    archivo.write(txt)
    archivo.close()

def cedulaEstudiante(estudiantes):
    while True:
        try:
            cedula = int(input("Ingrese el número de identificación del estudiante: "))
            estudiantes[cedula]
            return cedula
        except (ValueError, KeyError):
            print("Este estudiante no está registrado")

def nombreCurso(cursos):
    while True:
        curso = input("Ingrese el nombre del curso: ")
        try:
            cursos[curso]
            return curso
        except:
            print("Este curso no existe")

def printAdvice(string):
    print()
    print("*"*(len(string)+4)+f"\n* {string} *\n"+"*"*(len(string)+4))
    print()

def mostrarCursos(cursos):
    print("\nCURSOS")
    for i, j in cursos.items():
        print(f"\nNombre del curso: {i}\nNúmero de créditos: {j[0]}\nNúmero de notas: {j[1]}\nNúmero de estudiantes inscritos: {len(j[2])}\n")

def mostrarEstudiantes(estudiantes):
    print("\nESTUDIANTES")
    for i, j in estudiantes.items():
        print(f"\nNombre del estudiante: {j}\nNúmero de identificación: {i}\n")

def calcularPromedioPonderado(estudiante, cursos):
    sumatoria = 0
    creditos = 0
    for i, j in cursos.items():
        try:
            notaFinal = 0
            for nota in j[2][estudiante]:
                notaFinal += nota
            notaFinal = notaFinal/j[0]
            sumatoria += notaFinal*j[1]
            creditos += j[1]
        except KeyError:
            pass
    return sumatoria/creditos
