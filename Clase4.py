# Gestion de matriculas de DevSenior

estudiantes = []
cursos = ['Java', 'Python']
docentes = []
horarios = []

#Funciones para matricular un estudiante

def matricularEstudiante():

    nombre = input('Digite el nombre del estudiante: ')
    print('Seleccione el curso a matricular: ')

    for i, curso in enumerate(cursos):
        print(f'{i+1}: {curso}')

    cursoSeleccionado = int(input('Ingrese el numero del curso'))

    if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
        curso = cursos[cursoSeleccionado-1]
        estudiante = {'Nombre': nombre, 'Curso':curso}
        estudiantes.append(estudiante)
        print(f'Estudiante: {nombre}, matriculado en el curso: {curso}')

    else:
        print(f'Opcion de curso no valido, recuerde que solo hay {len(cursos)} cursos')

#Funcion para asignar los docentes a un curso

def asignarDocente():
    print('Seleccionar el curso al que desea asignar un docente: ')
    for i, curso in enumerate(cursos):
        print(f'{i+1}: {curso}')

    cursoSeleccionado = int(input('Ingrese el numero del curso'))
    if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
        curso = cursos[cursoSeleccionado-1]

        nombreDocente = input('Ingrese el nombre del docente: ')
        docente = {'Nombre': nombreDocente, 'Curso':curso}
        docentes.append(docente)
        print(f'Docente: {nombreDocente}, matriculado en el curso: {curso}')
    else:
        print(f'Opcion de curso no valido, recuerde que solo hay {len(cursos)} cursos')

#Funcion para asignar horario a un curso

def asignarHorario():
    print('Seleccionar el curso al que desea asignar el horario')
    for i, curso in enumerate(cursos):
        print(f'{i+1}: {curso}')
    cursoSeleccionado = int(input('Ingrese el numero del curso: '))
    if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
        curso = cursos[cursoSeleccionado-1]
        dias = input('Ingrese los dias de clase (ej: Martes y Jueves)')
        hora = input('Ingrese la hora de la clase (ej: 6 pm)')
        horario = {'curso': curso, 'dias': dias, 'hora': hora}
        horarios.append(horario)
        print(f'Horario asignado al curso: {curso}: {dias} a las {hora}')
    else:
        print(f'Opcion de curso no valido, recuerde que solo hay {len(cursos)} cursos')

def mostrarEstudiantes():
    if estudiantes:
            print('Lista de estudiantes matriculados ')
            for estudiante in estudiantes:
                print(f"Estudiante: {estudiante['Nombre']}, Curso: {estudiante['Curso']}")
    else:
            print('No hay estudiantes matriculados')

def mostrarDocentes():
    if docentes:
            print('Lista de docentes asignados ')
            for docente in docentes:
                print(f"Docente: {docente['Nombre']}, Curso: {docente['Curso']}")
    else:
            print('No hay docentes asignados')

def mostrarHorarios():
    if horarios:
            print('Horario de los cursos')
            for horario in horarios:
                print(f"Curso: {horario['curso']}, Dias : {horario['dias']}, Hora: {horario['hora']}")
    else:
            print('No hay horarios asignados')

while True:
        print('\n Sistema de matriculas de DevSenior')
        print('1. Matricular estudiante')
        print('2. Asignar docente a un curso')
        print('3. Asignar horario a un curso')
        print('4. Mostrar la lista de estudiantes matriculados')
        print('5. Mostrar la lista de docentes asignados')
        print('6. Mostrar horarios de los cursos ')
        print('7. Salir')

        opcion = int(input('digite la opcion: '))

        if opcion == 1:
            matricularEstudiante()
        elif opcion == 2:
            asignarDocente()
        elif opcion == 3:
            asignarHorario()
        elif opcion == 4:
            mostrarEstudiantes()
        elif opcion == 5:
            mostrarDocentes()
        elif opcion == 6:
            mostrarHorarios()
        elif opcion == 7:
            print('Gracias por usar el sistema de matriculas de DevSenior')
            break
        else:
            print('Opcion no valida, intente de nuevo')

