def cargarDatosEstudiantes(ruta):
    archivo = open(ruta, "r")
    data = archivo.readlines()
    archivo.close()
    estudiantes = {}
    for i in data:
        estudiantes[i.split(";")[0]] = i.split(";")[1][:-1]
    return estudiantes

def cargarDatosCursos(ruta):
    archivo = open(ruta, "r")
    data = archivo.read()
    archivo.close()
    cursos = {}
    data = data.split("\n\n")[:-1]
    for i in data:
        curso = i.split("\n")
        cursos[curso[0].split(";")[0]] = [curso[0].split(";")[1], curso[0].split(";")[2]]
        estudiantes = {}
        for j in curso[1:]:
            estudiantes[j.split(";")[0]] = j.split(";")[1:]
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
        except:
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
        except:
            pass
    while True:
        try:
            notas = int(input("Número de notas: "))
            break
        except:
            pass
    return nombre, creditos, notas

def actualizarCursos(ruta, datos):
    print(datos)
    archivo = open(ruta, "w")
    txt = ""
    for i, j in datos.items():
        txt += f"{i};{j[0]};{j[1]}\n"
        print(j[2])
        for k, l in j[2].items():
            txt += f"{k};"
            for n in l:
                txt += f"{n};"
            txt = txt[:-1]+"\n"
        txt += "\n"
    archivo.write(txt)
    archivo.close()
