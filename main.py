from funciones import *

estudiantes = cargarDatosEstudiantes("./students.txt")
cursos = cargarDatosCursos("./subjects.txt")

while True:
    menu = """
1. Agregar estudiante
2. Crear nuevo curso
3. Matricular estudiante en un curso
4. Mostrar todos los cursos registrados
5. Mostrar todos los estudiantes registrados
"""

    print(menu)

    op = int(input("Seleccione una opción: "))
    if op == 1:
        estudiante = agregarEstudiante()
        estudiantes[estudiante[0]] = estudiante[1]
        actualizarEstudiantes("./students.txt", estudiantes)
    elif op == 2:
        curso = crearNuevoCurso()
        cursos[curso[0]] = [curso[1], curso[2], {}]
        actualizarCursos("./subjects2.txt", cursos)
