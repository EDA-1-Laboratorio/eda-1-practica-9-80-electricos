# --- TUPLAS ---
print("=== TUPLAS ===")

# Crear tuplas
punto = (4, 7)
colores = ("rojo", "verde", "azul")

print("Punto:", punto)
print("Primer color:", colores[0])
print("Cantidad de colores:", len(colores))

# Desempaquetado (¡no existe en C!)
x, y = punto
print(f"x = {x}, y = {y}")

# --- DICCIONARIOS ---
print("\n=== DICCIONARIOS ===")

materia = {
    "nombre": "Estructura de Datos",
    "grupo": 4,
    "salon": "P-108",
    "alumnos": 35
}

print("Materia:", materia["nombre"])
print("Grupo:", materia["grupo"])

# Agregar una llave nueva
materia["semestre"] = "2026-2"
print("Diccionario completo:", materia)

# Obtener todas las llaves y valores
print("Llaves:", list(materia.keys()))
print("Valores:", list(materia.values()))
