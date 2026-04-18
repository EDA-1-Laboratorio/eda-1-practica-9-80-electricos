def agregar_producto(inventario):
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)
    print("Producto agregado.")

def mostrar_inventario(inventario):
    if not inventario:
        print("Inventario vacío.")
        return

    print(f"{'Nombre':<20} {'Precio':>10} {'Cantidad':>10}")
    print("-" * 42)

    for producto in inventario:
        print(f"{producto['nombre']:<20} {producto['precio']:>10.2f} {producto['cantidad']:>10}")

def buscar_producto(inventario, nombre):
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            return producto
    return None

def actualizar_cantidad(inventario):
    nombre = input("Nombre del producto: ")
    producto = buscar_producto(inventario, nombre)

    if producto:
        nueva_cantidad = int(input("Nueva cantidad: "))
        producto["cantidad"] = nueva_cantidad
        print("Cantidad actualizada.")
    else:
        print("Producto no encontrado.")

def eliminar_producto(inventario):
    nombre = input("Nombre del producto a eliminar: ")
    producto = buscar_producto(inventario, nombre)

    if producto:
        inventario.remove(producto)
        print("Producto eliminado.")
    else:
        print("Producto no encontrado.")

def resumen(inventario):
    if not inventario:
        print("Inventario vacío.")
        return

    total_productos = len(inventario)
    valor_total = sum(p["precio"] * p["cantidad"] for p in inventario)

    producto_caro = max(inventario, key=lambda p: p["precio"])
    producto_barato = min(inventario, key=lambda p: p["precio"])

    print("=== RESUMEN ===")
    print("Total de productos distintos:", total_productos)
    print("Valor total del inventario:", valor_total)
    print("Producto más caro:", producto_caro["nombre"], "-", producto_caro["precio"])
    print("Producto más barato:", producto_barato["nombre"], "-", producto_barato["precio"])

def menu():
    inventario = []

    while True:
        print("\n=== GESTOR DE INVENTARIO ===")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Actualizar cantidad")
        print("5. Eliminar producto")
        print("6. Resumen")
        print("7. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_producto(inventario)
        elif opcion == "2":
            mostrar_inventario(inventario)
        elif opcion == "3":
            nombre = input("Nombre a buscar: ")
            producto = buscar_producto(inventario, nombre)

            if producto:
                print(producto)
            else:
                print("No encontrado.")
        elif opcion == "4":
            actualizar_cantidad(inventario)
        elif opcion == "5":
            eliminar_producto(inventario)
        elif opcion == "6":
            resumen(inventario)
        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

menu()
