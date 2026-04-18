# Función simple
def area_rectangulo(base, altura):
    return base * altura

print("Área:", area_rectangulo(5, 3))

# Función con valor por defecto
def potencia(base, exponente=2):
    return base ** exponente

print("3^2 =", potencia(3))
print("2^10 =", potencia(2, 10))

# Función que retorna múltiples valores
def estadisticas(lista):
    minimo = min(lista)
    maximo = max(lista)
    promedio = sum(lista) / len(lista)
    return minimo, maximo, promedio

datos = [4, 8, 15, 16, 23, 42]
mn, mx, prom = estadisticas(datos)
print(f"Mín: {mn}, Máx: {mx}, Promedio: {prom}")
