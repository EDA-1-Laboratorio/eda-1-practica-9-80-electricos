# Lista con diferentes tipos (¡imposible en un arreglo de C!)
mixta = [1, "dos", 3.0, True, [5, 6]]
print("Lista mixta:", mixta)
print("Tipo:", type(mixta))

# Operaciones básicas
frutas = ["manzana", "naranja", "plátano"]
print("Original:", frutas)

frutas.append("uva")
print("Después de append:", frutas)

frutas.insert(1, "fresa")
print("Después de insert(1, 'fresa'):", frutas)

frutas.remove("naranja")
print("Después de remove('naranja'):", frutas)

ultimo = frutas.pop()
print("pop() devolvió:", ultimo)
print("Después de pop:", frutas)

print("Longitud:", len(frutas))
print("¿Está 'manzana'?:", "manzana" in frutas)
