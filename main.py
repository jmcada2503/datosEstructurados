from funciones import *

subjectsRoot = "./subjects.txt"
studentsRoot = "./students.txt"

estudiantes = cargarDatosEstudiantes(studentsRoot)
cursos = cargarDatosCursos(subjectsRoot)

print(cursos)
print(estudiantes)

while True:
    menu = """
1. Agregar estudiante
2. Crear nuevo curso
3. Matricular estudiante en un curso
4. Mostrar todos los cursos registrados
5. Mostrar todos los estudiantes registrados
6. Consultar promedio de estudiante
7. Consultar materias matriculadas por estudiante
8. Consultar estudiantes matriculados en un curso
9. Porcentaje de estudiantes que ganó y perdió un curso
10. Salir
"""

    print(menu)

    try:
        op = int(input("Seleccione una opción: "))
    except ValueError:
        op = None
    if op == 1:
        estudiante = agregarEstudiante()
        estudiantes[estudiante[0]] = estudiante[1]
        actualizarEstudiantes(studentsRoot, estudiantes)
    elif op == 2:
        curso = crearNuevoCurso()
        cursos[curso[0]] = [curso[1], curso[2], {}]
        actualizarCursos(subjectsRoot, cursos)
    elif op == 3:
        estudiante = cedulaEstudiante(estudiantes)
        curso = nombreCurso(cursos)
        try:
            cursos[curso][2][estudiante]
            printAdvice("Este estudiante ya está registrado en este curso")
        except:
            cursos[curso][2][estudiante] = []
            actualizarCursos(subjectsRoot, cursos)
    elif op == 4:
        mostrarCursos(cursos)
    elif op == 5:
        mostrarEstudiantes(estudiantes)
    elif op == 6:
        estudiante = cedulaEstudiante(estudiantes)
        promedio = calcularPromedioPonderado(estudiante, cursos)
        print(f"El promedio de este estudiante es: {round(promedio, 2)}")
    elif op == 7:
        estudiante = cedulaEstudiante(estudiantes)
        print("\nCursos en los que el estuidante está matriculado:\n")
        none = True
        for i, j in cursos.items():
            try:
                j[2][estudiante]
                print(i)
                none = False
            except KeyError:
                pass
        if none:
            print("Este estudiante no está matriculado en ningún curso")
    elif op == 8:
        curso = nombreCurso(cursos)
        if len(cursos[curso][2]) > 0:
            print(f"\nEstudiantes matriculados en {curso}:\n")
            for i in cursos[curso][2].keys():
                print(f"\nNombre del estudiante: {estudiantes[i]}\nNúmero de identificación del estudiante: {i}\n")
        else:
            print("\nNo existen estudiantes matriculados a este curso")
    elif op == 9:
        curso = nombreCurso(cursos)
        passed = 0
        for i in cursos[curso][2].values():
            nota = 0
            for j in i:
                nota += j
            nota = nota/cursos[curso][0]
            if nota >= 3:
                passed += 1
        print(f"\nEstudiantes que ganaron el curso: {(passed*100)/len(cursos[curso][2])}%\nEstudiantes que perdieron el curso: {100-((passed*100)/len(cursos[curso][2]))}%")
    elif op == 10:
        break
    else:
        print("Debes seleccionar una opción válida")
