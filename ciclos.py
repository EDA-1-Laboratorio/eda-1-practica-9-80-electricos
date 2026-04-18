# While: tabla de multiplicar
print("=== Tabla del 7 (while) ===")
i = 1
while i <= 10:
    print(f"7 x {i} = {7 * i}")
    i += 1

# For con range
print("\n=== Números del 0 al 9 ===")
for i in range(10):
    print(i, end=" ")
print()  # salto de línea

# For sobre lista
print("\n=== Iterando una lista ===")
materias = ["Cálculo", "Programación", "Física", "EDA"]
for materia in materias:
    print(f"  - {materia}")

# For con enumerate
print("\n=== Con índice ===")
for i, materia in enumerate(materias):
    print(f"  {i + 1}. {materia}")

# Iteración sobre un diccionario
print("\n=== Iterando un diccionario ===")
notas = {"Cálculo": 8.5, "Programación": 9.0, "Física": 7.5}
for materia, nota in notas.items():
    print(f"  {materia}: {nota}")
