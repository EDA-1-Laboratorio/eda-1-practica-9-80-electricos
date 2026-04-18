# Clasificación de triángulos por sus lados
def clasificar_triangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or b == c or a == c:
        return "Isósceles"
    else:
        return "Escaleno"

print(clasificar_triangulo(5, 5, 5))   # Equilátero
print(clasificar_triangulo(5, 5, 3))   # Isósceles
print(clasificar_triangulo(3, 4, 5))   # Escaleno
