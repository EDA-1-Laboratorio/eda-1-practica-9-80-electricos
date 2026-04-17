#Ejercicio 9.2 — Programa interactivo: Conversor de unidades

#Crea un archivo conversor.py. El programa pide al usuario un valor y le permite elegir el tipo de conversión:

print("=== Conversor de unidades ===")
print("1. Kilómetros a millas")
print("2. Millas a kilómetros")
print("3. Celsius a Fahrenheit")
print("4. Fahrenheit a Celsius")
print("5. Kilogramos a libras")
print("6. Libras a kilogramos")

opcion = input("Elige una opción (1-6): ")
valor = float(input("Ingresa el valor: "))

if opcion == "1":
    print(f"{valor} km = {valor * 0.621371:.4f} millas")
elif opcion == "2":
    print(f"{valor} millas = {valor * 1.60934:.4f} km")
elif opcion == "3":
    print(f"{valor}°C = {valor * 9/5 + 32:.2f}°F")
elif opcion == "4":
    print(f"{valor}°F = {(valor - 32) * 5/9:.2f}°C")
elif opcion == "5":
    print(f"{valor} kg = {valor * 2.20462:.4f} libras")
elif opcion == "6":
    print(f"{valor} libras = {valor * 0.453592:.4f} kg")
else:
    print("Opción no válida.")
