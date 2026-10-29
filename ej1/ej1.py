notas = {
    "Perez": [],
    "Herrazi": [],
    "Santilli": [],
    "Carrizo": [],
    "Almada": [],
}
while True:
    print("1. Ver todas las notas")
    print("2. Ver notas por alumno")
    print("3. Cargar notas")
    print("4. Promedio")
    print("5. Salir")
    opcion = input("Elija una opción: ")
    if opcion == "1":
        for apellido in notas:
            if len(notas[apellido]) > 0:
                print(apellido, ":", notas[apellido])
            else:
                print(apellido, ": sin notas")
    elif opcion == "2":
        apellido = input("Ingrese el apellido del alumno: ")
        if apellido in notas:
            if len(notas[apellido]) > 0:
                print("Notas de", apellido, ":", notas[apellido])
            else:
                print(apellido, "no tiene notas cargadas")
        else:
            print("El alumno no esta cargado")
    elif opcion == "3":
        apellido = input("Ingrese el apellido del alumno: ")
        if apellido in notas:
            notas[apellido] = []
            for i in range(5):
                nota = float(input("Nota: "))
                notas[apellido].append(nota)
            print("Notas cargadas")
        else:
            print("Error")
    elif opcion == "4":
        apellido = input("Ingrese el apellido del alumno: ")
        if apellido in notas:
            if len(notas[apellido]) > 0:
                promedio = sum(notas[apellido]) / len(notas[apellido])
                print("Promedio de", apellido, ":", round(promedio, 2))
            else:
                print(apellido, "no tiene notas")
        else:
            print("Error")
    elif opcion == "5":
        break