miembros = []
n = int(input("¿Cuántos miembros tiene el equipo? "))

for i in range(n):
    print(f"\n--- Miembro {i + 1} ---")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    lenguaje_fav = input("Lenguaje de programación favorito: ")

    miembros.append({
        "nombre": nombre,
        "edad": edad,
        "lenguaje": lenguaje_fav
    })

# Resumen
print("\n=== RESUMEN DEL EQUIPO ===")
print(f"{'Nombre':<15} {'Edad':>5} {'Lenguaje':<15}")
print("-" * 37)
for m in miembros:
    print(f"{m['nombre']:<15} {m['edad']:>5} {m['lenguaje']:<15}")

edades = [m["edad"] for m in miembros]
print(f"\nEdad promedio: {sum(edades) / len(edades):.1f}")

# Contar lenguajes
lenguajes = {}
for m in miembros:
    lang = m["lenguaje"]
    lenguajes[lang] = lenguajes.get(lang, 0) + 1

print("\nLenguajes favoritos:")
for lang, count in lenguajes.items():
    print(f"  {lang}: {count}")
