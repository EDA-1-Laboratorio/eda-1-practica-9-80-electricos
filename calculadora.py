print("=== Calculadora básica ===")
print("Operaciones: +, -, *, /")

num1 = float(input("Primer número: "))
operacion = input("Operación (+, -, *, /): ")
num2 = float(input("Segundo número: "))

if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Error: división entre cero")
        resultado = None
else:
    print("Operación no válida")
    resultado = None

if resultado is not None:
    print(f"{num1} {operacion} {num2} = {resultado}")
