def agregar_contacto(agenda):
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    # Crear diccionario y agregarlo a la agenda
    contacto = {
        "nombre": nombre,
        "telefono": telefono,
        "email": email
    }
    agenda.append(contacto)
    print("Contacto agregado a la agenda")


def listar_contactos(agenda):
    if not agenda:
        print("Agenda vacía")
        return
    # Ordenar por nombre e imprimir
    ordenados = sorted(agenda, key=lambda c: c["nombre"].lower())
    for c in ordenados:
        print(f"{c['nombre']} | {c['telefono']} | {c['email']}")


def buscar_contacto(agenda, termino):
    # Retornar lista de coincidencias
    return [c for c in agenda if termino.lower() in c["nombre"].lower()]


def editar_contacto(agenda):
    nombre = input("Nombre del contacto a editar: ")
    resultados = buscar_contacto(agenda, nombre)

    if not resultados:
        print("No existen resultados del contacto")
        return

    # Si hay múltiples resultados
    if len(resultados) > 1:
        print("Seleccione un contacto:")
        for i, c in enumerate(resultados):
            print(f"{i + 1}. {c['nombre']} - {c['telefono']} - {c['email']}")
        idx = int(input("Número: ")) - 1
        contacto = resultados[idx]
    else:
        contacto = resultados[0]

    # Editar datos
    nuevo_tel = input(f"Nuevo teléfono ({contacto['telefono']}): ")
    nuevo_email = input(f"Nuevo email ({contacto['email']}): ")

    if nuevo_tel:
        contacto["telefono"] = nuevo_tel
    if nuevo_email:
        contacto["email"] = nuevo_email

    print("Contacto actualizado")


def eliminar_contacto(agenda):
    nombre = input("Nombre del contacto a eliminar ")
    resultados = buscar_contacto(agenda, nombre)

    if not resultados:
        print("No se encontró contacto")
        return

    for c in resultados:
        agenda.remove(c)

    print("Contacto eliminado")


def exportar_csv(agenda):
    print("nombre,telefono,email")
    for c in agenda:
        print(f"{c['nombre']},{c['telefono']},{c['email']}")


def estadisticas(agenda):
    # Total de contactos
    print(f"Total de contactos: {len(agenda)}")

    # Contar dominios
    dominios = {}
    for c in agenda:
        if "@" in c["email"]:
            dominio = c["email"].split("@")[1]
            dominios[dominio] = dominios.get(dominio, 0) + 1

    if dominios:
        print("Dominios más comunes:")
        for d, count in sorted(dominios.items(), key=lambda x: x[1], reverse=True):
            print(f"{d}: {count}")


def menu():
    agenda = []
    while True:
        print("\n=== AGENDA DE CONTACTOS ===")
        print("1. Agregar contacto")
        print("2. Listar contactos")
        print("3. Buscar contacto")
        print("4. Editar contacto")
        print("5. Eliminar contacto")
        print("6. Exportar CSV")
        print("7. Estadísticas")
        print("8. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            listar_contactos(agenda)
        elif opcion == "3":
            termino = input("Buscar: ")
            resultados = buscar_contacto(agenda, termino)
            if resultados:
                for c in resultados:
                    print(f"  {c['nombre']} - {c['telefono']} - {c['email']}")
            else:
                print("Sin resultados.")
        elif opcion == "4":
            editar_contacto(agenda)
        elif opcion == "5":
            eliminar_contacto(agenda)
        elif opcion == "6":
            exportar_csv(agenda)
        elif opcion == "7":
            estadisticas(agenda)
        elif opcion == "8":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")


menu()

