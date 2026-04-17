[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/ITebWd05)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=23611379&assignment_repo_type=AssignmentRepo)
# EDAI - Práctica 09: Introducción al lenguaje de programación Python

## Objetivo

Introducir los fundamentos del lenguaje de programación Python.

## Actividades

- Ejemplificar el uso de variables y cadenas
- Probar el uso de operadores básicos
- Crear y manipular listas, tuplas y diccionarios
- Crear y ejecutar funciones
- Aplicar estructuras de control selectivas
- Aplicar estructuras de control repetitivas
- Ejemplificar el uso de alguna biblioteca
- Elaborar y ejecutar un programa que resuelva un problema sencillo

## Requisitos

- Python 3 instalado (verificar con `python3 --version` en terminal)
- Un editor de texto o IDE (VS Code, por ejemplo)

## Nota

A lo largo de esta práctica verás comparaciones frecuentes entre C y Python. Esto te
ayudará a conectar lo que ya sabes con la nueva sintaxis. Recuerda: en Python **la
indentación es obligatoria** y reemplaza a las llaves `{}` de C.

Para ejecutar cualquier archivo Python desde la terminal:

```bash
python3 nombre_archivo.py
```

También puedes usar el **intérprete interactivo** escribiendo solo `python3` en la terminal.
Esto abre una consola donde puedes probar instrucciones una por una (como una
calculadora). Para salir escribe `exit()`.

---

## Parte 1: Variables y tipos de datos

### Teoría

En C, declarar una variable requiere especificar su tipo:

```c
int edad = 20;
float promedio = 8.5;
char nombre[] = "Ana";
```

En Python, **no se especifica el tipo**; se infiere automáticamente al asignar un valor.
Tampoco se usa `;` al final de cada instrucción:

```python
edad = 20
promedio = 8.5
nombre = "Ana"
```

**Reglas para nombres de variables:**
- Son alfanuméricos (a-z, A-Z, 0-9) y comienzan con una letra minúscula.
- Las constantes se escriben por convención en MAYÚSCULAS: `PI = 3.14159`

**Palabras reservadas de Python** (no se pueden usar como nombres de variables):

`and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from,
global, if, import, in, is, lambda, not, or, pass, print, raise, return, try, while, with, yield`

Puedes conocer el tipo de una variable con la función `type()`:

```python
x = 42
print(type(x))    # <class 'int'>

y = 3.14
print(type(y))    # <class 'float'>

z = "hola"
print(type(z))    # <class 'str'>

w = True
print(type(w))    # <class 'bool'>
```

### Ejercicio 1.1 — Replica el ejemplo

Crea un archivo llamado `variables.py` y escribe el siguiente código. Ejecútalo y verifica
que la salida sea la esperada.

```python
# Variables numéricas
entero = 10
flotante = 3.14
booleano = True

# Verificar tipos
print(type(entero))
print(type(flotante))
print(type(booleano))

# Constante (convención)
GRAVEDAD = 9.81
print("La gravedad es:", GRAVEDAD)
```

**Salida esperada:**
```
<class 'int'>
<class 'float'>
<class 'bool'>
La gravedad es: 9.81
```

> **Tu turno:** Agrega una variable `nombre` con tu nombre y una variable `semestre` con
> tu semestre actual. Imprime ambas usando `print()`.

### Ejercicio 1.2 — Replica el ejemplo

Escribe y ejecuta el siguiente código que muestra la conversión entre tipos:

```python
# Conversión de tipos (casting)
entero = 7
flotante = float(entero)
print(flotante, type(flotante))   # 7.0 <class 'float'>

cadena_num = "42"
numero = int(cadena_num)
print(numero, type(numero))       # 42 <class 'int'>

pi = 3.14159
entero_pi = int(pi)
print(entero_pi, type(entero_pi)) # 3 <class 'int'>

# bool también es numérico
print(True + True)    # 2
print(False + 10)     # 10
print(int(True))      # 1
print(int(False))     # 0
```

> En C harías `(float)entero` o `atoi(cadena)`. En Python se usan las funciones `int()`,
> `float()`, `str()`, `bool()`.

### Ejercicio 1.3 — Replica el ejemplo

Escribe y ejecuta el siguiente código sobre asignación múltiple de variables:

```python
# Asignación múltiple (no existe en C)
a, b, c = 10, 20, 30
print(a, b, c)          # 10 20 30

# Intercambio de valores (en C necesitarías una variable temporal)
x = 100
y = 200
x, y = y, x
print(x, y)             # 200 100

# Misma asignación a varias variables
m = n = p = 0
print(m, n, p)          # 0 0 0
```

> En C, intercambiar dos variables requiere: `int temp = x; x = y; y = temp;`.
> En Python basta con `x, y = y, x`.

### Ejercicio 1.4 — Opción múltiple

¿Cuál de las siguientes declaraciones de variables es **incorrecta** en Python?

- a) `mi_variable = 100`
- b) `_temporal = "hola"`
- c) `int x = 5`
- d) `PI = 3.14159`

**Respuesta:** ______

### Ejercicio 1.5 — Opción múltiple

¿Qué imprime el siguiente código?

```python
x = 10
x = "diez"
print(type(x))
```

- a) `<class 'int'>`
- b) `<class 'str'>`
- c) Error: no se puede cambiar el tipo de una variable
- d) `<class 'float'>`

**Respuesta:** ______

> **Nota:** En C, una vez que declaras `int x`, esa variable siempre será `int`. En Python las
> variables pueden cambiar de tipo al reasignarles un valor. Esto se llama **tipado dinámico**.

### Ejercicio 1.6 — Opción múltiple

¿Cuál es el resultado de `int("3.14")`?

- a) `3`
- b) `3.14`
- c) Error: `ValueError`
- d) `"3"`

**Respuesta:** ______

> **Pista:** `int()` solo convierte cadenas que representan enteros. Para convertir `"3.14"` a
> entero, primero se debe hacer `int(float("3.14"))`.

### Ejercicio 1.7 — Opción múltiple

¿Qué imprime el siguiente código?

```python
a = 5
b = 2.0
c = a + b
print(type(c))
```

- a) `<class 'int'>`
- b) `<class 'float'>`
- c) `<class 'str'>`
- d) Error: no se pueden sumar un `int` y un `float`

**Respuesta:** ______

### Ejercicio 1.8 — Opción múltiple

¿Cuál de estas es una palabra reservada de Python que NO puedes usar como variable?

- a) `main`
- b) `printf`
- c) `lambda`
- d) `include`

**Respuesta:** ______

### Ejercicio 1.9 — Opción múltiple

¿Qué imprime el siguiente código?

```python
a, b = 5, 10
a, b = b, a
print(a, b)
```

- a) `5 10`
- b) `10 5`
- c) `10 10`
- d) Error

**Respuesta:** ______

---

## Parte 2: Cadenas

### Teoría

En C, las cadenas son arreglos de caracteres terminados en `'\0'`:

```c
char saludo[] = "Hola mundo";
printf("%s\n", saludo);
```

En Python, las cadenas se definen con comillas simples `'` o dobles `"` y son **inmutables**
(no se pueden modificar carácter por carácter):

```python
saludo = "Hola mundo"
print(saludo)
```

**Concatenación con `format()` y f-strings:**

```python
nombre = "Carlos"
edad = 20

# Estilo format()
print("Me llamo {} y tengo {} años".format(nombre, edad))

# Estilo f-string (Python 3.6+, más moderno)
print(f"Me llamo {nombre} y tengo {edad} años")
```

En C harías:
```c
printf("Me llamo %s y tengo %d años\n", nombre, edad);
```

**Operaciones útiles con cadenas:**

```python
texto = "Hola Mundo"
print(len(texto))          # 10  (longitud)
print(texto.upper())       # HOLA MUNDO
print(texto.lower())       # hola mundo
print(texto.replace("Mundo", "Python"))  # Hola Python
print(texto[0:4])          # Hola  (subcadena, índices 0 a 3)
```

### Ejercicio 2.1 — Replica el ejemplo

Crea un archivo `cadenas.py` con el siguiente código. Ejecútalo y verifica la salida.

```python
nombre = "Ada"
apellido = "Lovelace"

# Concatenación con +
print(nombre + " " + apellido)

# Concatenación con format
print("Nombre: {}, Apellido: {}".format(nombre, apellido))

# Cambiar orden con format
print("Apellido: {1}, Nombre: {0}".format(nombre, apellido))

# f-string
print(f"Programadora: {nombre} {apellido}")

# Caracteres de escape
print("Línea 1\nLínea 2")
print("Columna1\tColumna2")
```

### Ejercicio 2.2 — Replica el ejemplo

Escribe y ejecuta el siguiente código sobre operaciones con cadenas:

```python
mensaje = "  Estructura de Datos y Algoritmos  "

# Quitar espacios al inicio y final
print(mensaje.strip())

# Dividir una cadena en una lista (como strtok en C)
csv = "manzana,naranja,plátano,uva"
frutas = csv.split(",")
print(frutas)           # ['manzana', 'naranja', 'plátano', 'uva']

# Unir una lista en una cadena (operación inversa)
unida = " - ".join(frutas)
print(unida)            # manzana - naranja - plátano - uva

# Verificar contenido
print("datos" in mensaje)     # False
print(mensaje.startswith(" ")) # True

# Contar ocurrencias
texto = "abracadabra"
print(texto.count("a"))  # 5

# Encontrar posición (como strchr en C)
print(texto.find("cad"))  # 4 (índice donde empieza)
print(texto.find("xyz"))  # -1 (no encontrado)
```

### Ejercicio 2.3 — Replica el ejemplo

Escribe y ejecuta este código sobre slicing (rebanado) de cadenas:

```python
texto = "Python es genial"

# Slicing: texto[inicio:fin]  (fin NO se incluye)
print(texto[0:6])    # Python
print(texto[7:9])    # es
print(texto[10:])    # genial  (desde índice 10 hasta el final)
print(texto[:6])     # Python  (desde el inicio hasta índice 5)

# Índices negativos (cuenta desde el final)
print(texto[-6:])    # genial
print(texto[-6:-1])  # genia

# Slicing con paso: texto[inicio:fin:paso]
print(texto[::2])    # Pto sgna  (cada 2 caracteres)

# Invertir una cadena (¡muy útil!)
print(texto[::-1])   # laineg se nohtyP

# Repetir cadenas con *
print("ja" * 3)      # jajaja
print("-" * 30)      # ------------------------------
```

> En C, invertir una cadena requiere un ciclo. En Python basta con `texto[::-1]`.

### Ejercicio 2.4 — Completa el código

Completa las líneas marcadas con `???` para que el programa funcione correctamente:

```python
fruta = "manzana"

# Imprimir la longitud de la cadena
print("La fruta tiene", ???(fruta), "letras")

# Imprimir en mayúsculas
print(fruta.???())

# Imprimir los primeros 3 caracteres
print(fruta[???])
```

**Salida esperada:**
```
La fruta tiene 7 letras
MANZANA
man
```

### Ejercicio 2.5 — Completa el código

Completa el código para generar un acrónimo a partir de una frase:

```python
frase = "Estructura de Datos y Algoritmos"

palabras = frase.???(???)   # Dividir la frase en palabras
acronimo = ""

for palabra in palabras:
    acronimo = acronimo + palabra[???].???()   # Primera letra en mayúscula

print(acronimo)
```

**Salida esperada:**
```
EDDYA
```

> **Pistas:** `split()` separa por espacios, `[0]` obtiene el primer carácter, `upper()` convierte
> a mayúscula.

### Ejercicio 2.6 — Completa el código

Completa el código que verifica si una cadena es un palíndromo (se lee igual al derecho
y al revés):

```python
def es_palindromo(texto):
    texto = texto.???()        # Convertir a minúsculas
    texto = texto.replace(" ", "")  # Quitar espacios
    return texto == texto[???]      # Comparar con la cadena invertida

# Pruebas
print(es_palindromo("anilina"))      # True
print(es_palindromo("Reconocer"))    # True
print(es_palindromo("Python"))       # False
print(es_palindromo("Oso"))          # True
```

### Ejercicio 2.7 — Opción múltiple

¿Qué sucede si intentas ejecutar lo siguiente?

```python
texto = "Hola"
texto[0] = "h"
```

- a) Cambia la `H` por `h` y `texto` ahora vale `"hola"`
- b) Se genera un error porque las cadenas son inmutables
- c) Se crea una nueva cadena `"hola"` automáticamente
- d) No pasa nada, el cambio se ignora silenciosamente

**Respuesta:** ______

### Ejercicio 2.8 — Opción múltiple

¿Qué imprime el siguiente código?

```python
texto = "Hola Mundo"
print(texto.split())
```

- a) `"Hola Mundo"`
- b) `['H', 'o', 'l', 'a', ' ', 'M', 'u', 'n', 'd', 'o']`
- c) `['Hola', 'Mundo']`
- d) `('Hola', 'Mundo')`

**Respuesta:** ______

### Ejercicio 2.9 — Opción múltiple

¿Qué imprime el siguiente código?

```python
s = "Python"
print(s[-1], s[-2])
```

- a) `P y`
- b) `n o`
- c) Error: los índices negativos no existen
- d) `n h`

**Respuesta:** ______

---

## Parte 3: Operadores

### Teoría

Los operadores en Python son muy similares a los de C, con algunas diferencias notables:

| Operación         | C               | Python          |
|-------------------|-----------------|-----------------|
| Suma              | `a + b`         | `a + b`         |
| Resta             | `a - b`         | `a - b`         |
| Multiplicación    | `a * b`         | `a * b`         |
| División real     | `(float)a / b`  | `a / b`         |
| División entera   | `a / b`         | `a // b`        |
| Módulo            | `a % b`         | `a % b`         |
| Potencia          | `pow(a, b)`     | `a ** b`        |
| AND lógico        | `a && b`        | `a and b`       |
| OR lógico         | `a \|\| b`      | `a or b`        |
| NOT lógico        | `!a`            | `not a`         |

> **Diferencia importante:** En C, `7 / 2` da `3` (división entera entre enteros). En Python,
> `7 / 2` da `3.5` (siempre división real). Para obtener división entera en Python, usa `//`.

### Ejercicio 3.1 — Replica el ejemplo

Crea un archivo `operadores.py`:

```python
a = 15
b = 4

print("Suma:", a + b)         # 19
print("Resta:", a - b)        # 11
print("Multiplicación:", a * b) # 60
print("División real:", a / b)  # 3.75
print("División entera:", a // b) # 3
print("Módulo:", a % b)        # 3
print("Potencia:", a ** b)     # 50625

# Operadores booleanos
x = True
y = False
print("x and y:", x and y)    # False
print("x or y:", x or y)      # True
print("not x:", not x)        # False

# Comparación
print("15 > 4:", a > b)       # True
print("15 == 4:", a == b)     # False
print("15 != 4:", a != b)     # True
```

### Ejercicio 3.2 — Replica el ejemplo

Escribe y ejecuta el siguiente código sobre operadores de asignación compuesta:

```python
# Operadores de asignación compuesta (igual que en C, excepto ++ y --)
x = 10
print("Valor inicial:", x)  # 10

x += 5     # x = x + 5
print("x += 5 →", x)       # 15

x -= 3     # x = x - 3
print("x -= 3 →", x)       # 12

x *= 2     # x = x * 2
print("x *= 2 →", x)       # 24

x //= 5   # x = x // 5
print("x //= 5 →", x)      # 4

x **= 3   # x = x ** 3
print("x **= 3 →", x)      # 64

x %= 10   # x = x % 10
print("x %= 10 →", x)       # 4

# ¡CUIDADO! NO existe ++ ni -- en Python
# i++   → Error de sintaxis
# i--   → Error de sintaxis
# Usa:  i += 1  o  i -= 1
```

> En C puedes usar `x++`. En Python debes escribir `x += 1`.

### Ejercicio 3.3 — Replica el ejemplo

Escribe y ejecuta el siguiente código que muestra particularidades de los operadores
en Python:

```python
# Comparaciones encadenadas (¡no existen en C!)
edad = 20
print(18 <= edad <= 25)    # True  (en C: edad >= 18 && edad <= 25)

nota = 8.5
print(6.0 <= nota <= 10.0) # True

# Operador "in" (no existe en C)
vocales = "aeiou"
print("a" in vocales)      # True
print("x" in vocales)      # False

# Operador is (identidad, no igualdad)
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b)   # True  (mismo contenido)
print(a is b)   # False (distintos objetos en memoria)
print(a is c)   # True  (mismo objeto en memoria)

# Operador * con cadenas y listas
print("hola " * 3)         # hola hola hola
print([0] * 5)             # [0, 0, 0, 0, 0]
```

### Ejercicio 3.4 — Opción múltiple

¿Cuál es el resultado de la siguiente expresión en Python?

```python
print(7 / 2, 7 // 2, 7 % 2)
```

- a) `3 3 1`
- b) `3.5 3 1`
- c) `3.5 3.0 1`
- d) `3.5 3 1.0`

**Respuesta:** ______

### Ejercicio 3.5 — Opción múltiple

¿Qué imprime el siguiente código?

```python
print(2 ** 10)
```

- a) `20`
- b) `1024`
- c) `100`
- d) Error: el operador `**` no existe

**Respuesta:** ______

### Ejercicio 3.6 — Opción múltiple

¿Qué imprime el siguiente código?

```python
x = 10
x += 5
x *= 2
print(x)
```

- a) `25`
- b) `30`
- c) `35`
- d) `20`

**Respuesta:** ______

### Ejercicio 3.7 — Opción múltiple

¿Cuál de estos operadores **NO** existe en Python?

- a) `**`
- b) `//`
- c) `++`
- d) `%`

**Respuesta:** ______

### Ejercicio 3.8 — Opción múltiple

¿Qué imprime el siguiente código?

```python
print(10 == 10.0)
print(10 is 10.0)
```

- a) `True` y `True`
- b) `True` y `False`
- c) `False` y `False`
- d) `False` y `True`

**Respuesta:** ______

> **Nota:** `==` compara valores; `is` compara si son el mismo objeto en memoria.
> `10` (int) y `10.0` (float) tienen el mismo valor pero son objetos distintos.

### Ejercicio 3.9 — Opción múltiple

¿Qué imprime el siguiente código?

```python
print(5 < 10 < 20)
print(5 < 10 > 3)
```

- a) `True` y `True`
- b) `True` y `False`
- c) `True` y Error
- d) Error y Error

**Respuesta:** ______

---

## Parte 4: Listas

### Teoría

Las listas en Python son el equivalente más cercano a los **arreglos** de C, pero mucho más
flexibles:

| Característica           | C (arreglos)                    | Python (listas)              |
|--------------------------|---------------------------------|------------------------------|
| Declaración              | `int arr[5] = {1,2,3,4,5};`    | `arr = [1, 2, 3, 4, 5]`     |
| Tamaño                   | Fijo en compilación             | Dinámico                     |
| Tipos de elementos       | Todos del mismo tipo            | Pueden ser de tipos mixtos   |
| Acceso por índice        | `arr[0]`                        | `arr[0]`                     |
| Mutabilidad              | Sí                              | Sí                           |

```python
# Crear una lista
numeros = [10, 20, 30, 40, 50]

# Acceder a elementos (igual que en C)
print(numeros[0])    # 10
print(numeros[-1])   # 50  (¡último elemento! No existe en C)

# Modificar un elemento
numeros[2] = 99
print(numeros)       # [10, 20, 99, 40, 50]

# Agregar al final
numeros.append(60)
print(numeros)       # [10, 20, 99, 40, 50, 60]

# Longitud
print(len(numeros))  # 6

# Sublistas (slicing)
print(numeros[1:4])  # [20, 99, 40]  (índice 1 al 3)
```

### Ejercicio 4.1 — Replica el ejemplo

Crea un archivo `listas.py`:

```python
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
```

### Ejercicio 4.2 — Replica el ejemplo

Escribe y ejecuta el siguiente código sobre slicing y copia de listas:

```python
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Slicing
print(numeros[2:5])     # [2, 3, 4]
print(numeros[:3])      # [0, 1, 2]     (primeros 3)
print(numeros[-3:])     # [7, 8, 9]     (últimos 3)
print(numeros[::2])     # [0, 2, 4, 6, 8]  (cada 2)
print(numeros[::-1])    # [9, 8, 7, ..., 0] (invertida)

# ¡CUIDADO con las copias!
# Asignación NO copia, ambas apuntan al mismo objeto
a = [1, 2, 3]
b = a
b[0] = 99
print("a:", a)  # a: [99, 2, 3]  ← ¡a también cambió!

# Para hacer una copia independiente:
c = [1, 2, 3]
d = c.copy()    # o también: d = c[:]
d[0] = 99
print("c:", c)  # c: [1, 2, 3]  ← c no cambió
print("d:", d)  # d: [99, 2, 3]
```

> En C, asignar un arreglo a otro también copia la dirección (con punteros). El
> comportamiento es similar, pero en Python la solución es más sencilla: `.copy()`.

### Ejercicio 4.3 — Replica el ejemplo

Escribe y ejecuta el siguiente código sobre list comprehensions (una forma compacta
de crear listas, sin equivalente directo en C):

```python
# Crear una lista con los cuadrados del 1 al 10
# Forma clásica (como en C):
cuadrados = []
for i in range(1, 11):
    cuadrados.append(i ** 2)
print("Clásica:", cuadrados)

# Forma con list comprehension (exclusiva de Python):
cuadrados = [i ** 2 for i in range(1, 11)]
print("Comprehension:", cuadrados)

# Filtrar: solo los pares
pares = [x for x in range(1, 21) if x % 2 == 0]
print("Pares:", pares)

# Transformar: longitud de cada palabra
palabras = ["hola", "mundo", "python", "es", "genial"]
longitudes = [len(p) for p in palabras]
print("Longitudes:", longitudes)  # [4, 5, 6, 2, 6]
```

### Ejercicio 4.4 — Completa el código

Dada la siguiente lista, completa el código para obtener la salida indicada:

```python
calificaciones = [8.5, 9.0, 7.5, 10.0, 6.0, 8.0]

# 1. Imprime la cantidad de calificaciones
print("Total:", ???)

# 2. Imprime la calificación más alta
print("Máxima:", ???)

# 3. Imprime la calificación más baja
print("Mínima:", ???)

# 4. Imprime el promedio
print("Promedio:", ???)

# 5. Imprime las calificaciones ordenadas de menor a mayor
#    Pista: usa sorted()
print("Ordenadas:", ???)
```

**Salida esperada:**
```
Total: 6
Máxima: 10.0
Mínima: 6.0
Promedio: 8.166666666666666
Ordenadas: [6.0, 7.5, 8.0, 8.5, 9.0, 10.0]
```

> **Pistas:** `len()`, `max()`, `min()`, `sum()`, `sorted()` son funciones integradas de Python.

### Ejercicio 4.5 — Completa el código

Completa el código que combina dos listas en una lista de tuplas (como un "zip"):

```python
nombres = ["Ana", "Luis", "María", "Pedro"]
edades = [20, 22, 19, 21]

# Combinar usando zip()
combinada = list(???(nombres, edades))
print(combinada)
# [('Ana', 20), ('Luis', 22), ('María', 19), ('Pedro', 21)]

# Encontrar el nombre de la persona más joven
edad_minima = ???(edades)
indice_joven = edades.???(edad_minima)
print(f"El más joven es {nombres[indice_joven]} con {edad_minima} años")
```

**Salida esperada:**
```
[('Ana', 20), ('Luis', 22), ('María', 19), ('Pedro', 21)]
El más joven es María con 19 años
```

### Ejercicio 4.6 — Completa el código

Completa el código que usa list comprehension para filtrar y transformar datos:

```python
temperaturas_f = [32, 50, 68, 86, 104, 212]

# Convertir todas a Celsius: C = (F - 32) * 5/9
temperaturas_c = [??? for f in temperaturas_f]
print("En Celsius:", temperaturas_c)

# Filtrar solo las temperaturas menores a 50°C
frias = [c for c in temperaturas_c if ???]
print("Menores a 50°C:", frias)
```

**Salida esperada:**
```
En Celsius: [0.0, 10.0, 20.0, 30.0, 40.0, 100.0]
Menores a 50°C: [0.0, 10.0, 20.0, 30.0, 40.0]
```

### Ejercicio 4.7 — Opción múltiple

¿Qué imprime el siguiente código?

```python
lista = [1, 2, 3, 4, 5]
print(lista[1:3])
```

- a) `[1, 2, 3]`
- b) `[2, 3]`
- c) `[2, 3, 4]`
- d) `[1, 2]`

**Respuesta:** ______

### Ejercicio 4.8 — Opción múltiple

¿Qué imprime este código?

```python
lista = [10, 20, 30]
lista.append([40, 50])
print(len(lista))
```

- a) `3`
- b) `4`
- c) `5`
- d) Error

**Respuesta:** ______

> **Nota:** `append` agrega el argumento como **un solo elemento**. Si quieres agregar los
> elementos individuales, usa `extend`: `lista.extend([40, 50])` → longitud sería 5.

### Ejercicio 4.9 — Opción múltiple

¿Qué imprime este código?

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
```

- a) `[1, 2, 3]`
- b) `[1, 2, 3, 4]`
- c) Error: `b` es una copia, no se puede modificar `a`
- d) `[4, 1, 2, 3]`

**Respuesta:** ______

### Ejercicio 4.10 — Opción múltiple

¿Qué produce la siguiente list comprehension?

```python
result = [x * 2 for x in range(5)]
print(result)
```

- a) `[0, 1, 2, 3, 4]`
- b) `[2, 4, 6, 8, 10]`
- c) `[0, 2, 4, 6, 8]`
- d) `[1, 2, 3, 4, 5]`

**Respuesta:** ______

### Ejercicio 4.11 — Opción múltiple

¿Qué imprime el siguiente código?

```python
lista = [1, 2, 3, 4, 5]
print(lista[-2])
```

- a) `2`
- b) `4`
- c) `5`
- d) Error: índice negativo no válido

**Respuesta:** ______

### Ejercicio 4.12 — Opción múltiple

¿Qué imprime el siguiente código?

```python
nums = [3, 1, 4, 1, 5]
nums.sort()
print(nums)
nums.reverse()
print(nums)
```

- a) `[1, 1, 3, 4, 5]` y `[5, 4, 3, 1, 1]`
- b) `[3, 1, 4, 1, 5]` y `[5, 1, 4, 1, 3]`
- c) `[1, 1, 3, 4, 5]` y `[1, 1, 3, 4, 5]`
- d) Error: no se puede ordenar una lista con duplicados

**Respuesta:** ______

---

## Parte 5: Tuplas y diccionarios

### Teoría — Tuplas

Las tuplas son **similares a las listas**, pero son **inmutables** (no se pueden modificar después
de crearlas). Son más eficientes en memoria.

```python
# Crear una tupla
coordenada = (3, 5)
dias = ("lunes", "martes", "miércoles")

# Acceso por índice (igual que listas)
print(coordenada[0])   # 3
print(dias[1])         # martes

# ¡Esto genera error!
# coordenada[0] = 10   # TypeError: 'tuple' object does not support item assignment
```

Comparación con C: En C no existe un equivalente directo de las tuplas. Lo más cercano
sería `struct` de solo lectura, pero sin protección real de inmutabilidad.

### Teoría — Diccionarios

Un diccionario almacena pares **llave: valor**. Es similar a una tabla hash.

```python
# Crear un diccionario
alumno = {
    "nombre": "María",
    "carrera": "Computación",
    "semestre": 2,
    "promedio": 9.1
}

# Acceder a un valor
print(alumno["nombre"])     # María

# Modificar un valor
alumno["semestre"] = 3

# Agregar un nuevo par
alumno["grupo"] = "A"

# Verificar si una llave existe
print("nombre" in alumno)   # True
```

Equivalente en C: Lo más parecido sería un `struct`, pero los diccionarios son dinámicos.

```c
// En C necesitarías:
struct Alumno {
    char nombre[50];
    char carrera[50];
    int semestre;
    float promedio;
};
```

### Ejercicio 5.1 — Replica el ejemplo

Crea un archivo `tuplas_diccionarios.py`:

```python
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
```

### Ejercicio 5.2 — Replica el ejemplo

Escribe y ejecuta el siguiente código sobre operaciones avanzadas con diccionarios:

```python
# Método get() — evita errores si la llave no existe
alumno = {"nombre": "Juan", "edad": 20}

print(alumno.get("nombre"))         # Juan
print(alumno.get("telefono"))       # None (no lanza error)
print(alumno.get("telefono", "N/A")) # N/A (valor por defecto)

# En contraste, esto SÍ lanza error:
# print(alumno["telefono"])  → KeyError

# Eliminar un par llave:valor
del alumno["edad"]
print(alumno)  # {"nombre": "Juan"}

# Combinar dos diccionarios
datos1 = {"a": 1, "b": 2}
datos2 = {"b": 20, "c": 30}
datos1.update(datos2)
print(datos1)  # {"a": 1, "b": 20, "c": 30}  (b se sobreescribe)

# Diccionario a partir de listas con zip
llaves = ["nombre", "edad", "carrera"]
valores = ["Ana", 19, "Computación"]
diccionario = dict(zip(llaves, valores))
print(diccionario)
```

### Ejercicio 5.3 — Replica el ejemplo

Escribe y ejecuta el siguiente código sobre tuplas con nombre (namedtuple):

```python
from collections import namedtuple

# Definir una tupla con nombre (similar a un struct de C)
Punto = namedtuple("Punto", ["x", "y"])
Alumno = namedtuple("Alumno", ["nombre", "carrera", "semestre"])

# Crear instancias
p = Punto(3, 7)
a = Alumno("Carlos", "Computación", 2)

# Acceso por nombre (como en un struct)
print(f"Punto: ({p.x}, {p.y})")
print(f"Alumno: {a.nombre}, {a.carrera}, semestre {a.semestre}")

# También se puede acceder por índice
print(f"Coordenada x: {p[0]}")

# Son inmutables (como las tuplas normales)
# p.x = 10  → AttributeError
```

> En C esto sería exactamente un `struct Punto { int x; int y; };` pero con la ventaja
> de que es inmutable.

### Ejercicio 5.4 — Completa el código

Completa el siguiente programa que usa un diccionario para contar la frecuencia de cada
letra en una cadena:

```python
texto = "abracadabra"
frecuencia = {}

for letra in texto:
    if letra in frecuencia:
        frecuencia[???] = frecuencia[???] + 1
    else:
        frecuencia[???] = 1

print(frecuencia)
```

**Salida esperada:**
```
{'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
```

### Ejercicio 5.5 — Completa el código

Completa el código que invierte un diccionario (las llaves se vuelven valores y viceversa):

```python
original = {"rojo": 1, "verde": 2, "azul": 3}

invertido = {}
for llave, valor in original.???():
    invertido[???] = ???

print(invertido)
```

**Salida esperada:**
```
{1: 'rojo', 2: 'verde', 3: 'azul'}
```

### Ejercicio 5.6 — Completa el código

Completa el código que agrupa una lista de tuplas `(nombre, materia)` en un diccionario
donde la llave es la materia y el valor es la lista de alumnos:

```python
inscripciones = [
    ("Ana", "EDA"),
    ("Luis", "Cálculo"),
    ("María", "EDA"),
    ("Pedro", "Física"),
    ("Ana", "Cálculo"),
    ("Luis", "EDA"),
]

por_materia = {}
for nombre, materia in inscripciones:
    if materia not in por_materia:
        por_materia[???] = []
    por_materia[???].???(nombre)

for materia, alumnos in por_materia.items():
    print(f"  {materia}: {alumnos}")
```

**Salida esperada:**
```
  EDA: ['Ana', 'María', 'Luis']
  Cálculo: ['Luis', 'Ana']
  Física: ['Pedro']
```

### Ejercicio 5.7 — Opción múltiple

¿Cuál es la diferencia principal entre una lista y una tupla?

- a) Las listas usan `[]` y las tuplas usan `()`, pero se comportan igual
- b) Las listas son mutables y las tuplas son inmutables
- c) Las tuplas pueden contener más tipos de datos que las listas
- d) Las listas son más rápidas que las tuplas

**Respuesta:** ______

### Ejercicio 5.8 — Opción múltiple

¿Qué imprime el siguiente código?

```python
d = {"a": 1, "b": 2, "c": 3}
d["b"] = 20
print(d)
```

- a) `{"a": 1, "b": 2, "c": 3, "b": 20}`
- b) `{"a": 1, "b": 20, "c": 3}`
- c) Error: no se pueden modificar los valores de un diccionario
- d) `{"a": 1, "c": 3, "b": 20}`

**Respuesta:** ______

### Ejercicio 5.9 — Opción múltiple

¿Qué imprime el siguiente código?

```python
d = {"x": 10, "y": 20}
print(d.get("z", 0))
```

- a) `None`
- b) `0`
- c) Error: `KeyError`
- d) `"z"`

**Respuesta:** ______

### Ejercicio 5.10 — Opción múltiple

¿Qué imprime el siguiente código?

```python
tupla = (1, 2, 3)
lista = list(tupla)
lista.append(4)
print(tupla, lista)
```

- a) `(1, 2, 3, 4) [1, 2, 3, 4]`
- b) `(1, 2, 3) [1, 2, 3, 4]`
- c) Error: no se puede convertir una tupla a lista
- d) `(1, 2, 3) [1, 2, 3]`

**Respuesta:** ______

### Ejercicio 5.11 — Opción múltiple

¿Qué imprime `len(d)` si `d = {"a": 1, "b": [2, 3, 4], "c": "hola"}`?

- a) `3`
- b) `6`
- c) `8`
- d) Error

**Respuesta:** ______

### Ejercicio 5.12 — Opción múltiple

¿Cuál de estos NO puede ser una llave de diccionario?

- a) `42`
- b) `"hola"`
- c) `(1, 2)`
- d) `[1, 2]`

**Respuesta:** ______

> **Nota:** Las llaves de un diccionario deben ser **inmutables**. Las listas son mutables,
> por lo que no pueden usarse como llaves. Enteros, cadenas y tuplas sí pueden.

---

## Parte 6: Funciones

### Teoría

En C, una función requiere especificar tipos de retorno y de parámetros:

```c
int suma(int a, int b) {
    return a + b;
}
```

En Python, se usa la palabra clave `def`, sin tipos:

```python
def suma(a, b):
    return a + b
```

**Diferencias clave:**
- No se declara el tipo de retorno ni el de los parámetros.
- El cuerpo se delimita por **indentación**, no por `{}`.
- Una función puede **retornar múltiples valores** (como una tupla).

```python
def dividir(a, b):
    cociente = a // b
    residuo = a % b
    return cociente, residuo

c, r = dividir(17, 5)
print(f"Cociente: {c}, Residuo: {r}")
```

**Valores por defecto** (no existen en C estándar):

```python
def saludar(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}!")

saludar("Ana")            # Hola, Ana!
saludar("Ana", "Buenos días")  # Buenos días, Ana!
```

### Ejercicio 6.1 — Replica el ejemplo

Crea un archivo `funciones.py`:

```python
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
```

### Ejercicio 6.2 — Replica el ejemplo

Escribe y ejecuta el siguiente código sobre funciones con argumentos variables:

```python
# Función con número variable de argumentos (*args)
def sumar_todos(*numeros):
    total = 0
    for n in numeros:
        total += n
    return total

print(sumar_todos(1, 2, 3))         # 6
print(sumar_todos(10, 20, 30, 40))   # 100

# Función con argumentos nombrados (**kwargs)
def crear_perfil(**datos):
    for llave, valor in datos.items():
        print(f"  {llave}: {valor}")

print("Perfil:")
crear_perfil(nombre="Ana", edad=20, carrera="Computación")
```

> En C, las funciones con argumentos variables (`...`) son complicadas (requieren `stdarg.h`).
> En Python es directo con `*args` y `**kwargs`.

### Ejercicio 6.3 — Replica el ejemplo

Escribe y ejecuta el siguiente código sobre funciones lambda (anónimas):

```python
# Función lambda: función de una sola expresión
doble = lambda x: x * 2
print(doble(5))   # 10

# Útil para ordenar con criterio personalizado
alumnos = [
    {"nombre": "Carlos", "promedio": 8.5},
    {"nombre": "Ana", "promedio": 9.2},
    {"nombre": "Luis", "promedio": 7.8},
]

# Ordenar por promedio (de mayor a menor)
alumnos_ordenados = sorted(alumnos, key=lambda a: a["promedio"], reverse=True)
for a in alumnos_ordenados:
    print(f"  {a['nombre']}: {a['promedio']}")

# map: aplica una función a cada elemento
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print("Cuadrados:", cuadrados)   # [1, 4, 9, 16, 25]

# filter: filtra elementos que cumplen una condición
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Pares:", pares)           # [2, 4]
```

### Ejercicio 6.4 — Completa el código

Completa la función que convierte grados Celsius a Fahrenheit y viceversa:

```python
def celsius_a_fahrenheit(celsius):
    return ???

def fahrenheit_a_celsius(fahrenheit):
    return ???

# Pruebas
print(celsius_a_fahrenheit(0))     # 32.0
print(celsius_a_fahrenheit(100))   # 212.0
print(fahrenheit_a_celsius(32))    # 0.0
print(fahrenheit_a_celsius(212))   # 100.0
```

> **Recuerda:** $F = C \times \frac{9}{5} + 32$ y $C = (F - 32) \times \frac{5}{9}$

### Ejercicio 6.5 — Completa el código

Escribe una función que reciba una lista de números y retorne **dos listas**: una con
los números pares y otra con los impares.

```python
def separar_pares_impares(numeros):
    pares = []
    impares = []
    for n in numeros:
        if ???:
            pares.???(n)
        else:
            impares.???(n)
    return pares, impares

# Prueba
datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
p, i = separar_pares_impares(datos)
print("Pares:", p)      # [2, 4, 6, 8, 10]
print("Impares:", i)    # [1, 3, 5, 7, 9]
```

### Ejercicio 6.6 — Completa el código

Completa la función que cuenta cuántas vocales y consonantes tiene una cadena:

```python
def contar_vocales_consonantes(texto):
    vocales = "aeiouáéíóú"
    texto = texto.???()  # Convertir a minúsculas
    num_vocales = 0
    num_consonantes = 0
    for c in texto:
        if c.isalpha():    # Solo letras (ignora espacios, números, etc.)
            if c ??? vocales:
                num_vocales ???= 1
            else:
                num_consonantes += 1
    return num_vocales, num_consonantes

# Pruebas
v, c = contar_vocales_consonantes("Hola Mundo")
print(f"Vocales: {v}, Consonantes: {c}")  # Vocales: 4, Consonantes: 5

v, c = contar_vocales_consonantes("Python")
print(f"Vocales: {v}, Consonantes: {c}")  # Vocales: 1, Consonantes: 5
```

### Ejercicio 6.7 — Completa el código

Completa la función que recibe una lista de diccionarios y retorna el que tenga
el mayor valor en una llave dada:

```python
def encontrar_maximo(lista, llave):
    if not lista:
        return None
    maximo = lista[???]
    for elemento in lista:
        if elemento[???] > maximo[???]:
            maximo = elemento
    return maximo

# Pruebas
productos = [
    {"nombre": "Laptop", "precio": 15000},
    {"nombre": "Teclado", "precio": 500},
    {"nombre": "Monitor", "precio": 8000},
    {"nombre": "Mouse", "precio": 300},
]

caro = encontrar_maximo(productos, "precio")
print(f"Más caro: {caro['nombre']} (${caro['precio']})")
# Más caro: Laptop ($15000)
```

### Ejercicio 6.8 — Completa el código

Completa la función recursiva que calcula la potencia de un número:

```python
def potencia_recursiva(base, exponente):
    if exponente == ???:
        return ???
    return base * potencia_recursiva(???, ???)

# Pruebas
print(potencia_recursiva(2, 10))   # 1024
print(potencia_recursiva(3, 4))    # 81
print(potencia_recursiva(5, 0))    # 1
```

### Ejercicio 6.9 — Completa el código

Completa la función que elimina los duplicados de una lista manteniendo el orden
original:

```python
def eliminar_duplicados(lista):
    vistos = ???      # Pista: usa un conjunto (set)
    resultado = []
    for elemento in lista:
        if elemento ??? vistos:
            resultado.append(elemento)
            vistos.???(elemento)
    return resultado

# Pruebas
print(eliminar_duplicados([1, 3, 2, 1, 5, 3, 2, 4]))
# [1, 3, 2, 5, 4]
print(eliminar_duplicados(["a", "b", "a", "c", "b"]))
# ['a', 'b', 'c']
```

> **Pista:** Un `set()` es una colección sin duplicados. Puedes usar `not in` para verificar si
> un elemento NO está en el conjunto, y `.add()` para agregar elementos.

### Ejercicio 6.10 — Variables globales y locales (I)

Estudia el siguiente código y **sin ejecutarlo**, predice qué se imprime. Luego verifica
ejecutándolo.

```python
x = 100  # Variable global

def modificar():
    x = 50   # Variable local (¡no modifica la global!)
    print("Dentro de la función, x =", x)

modificar()
print("Fuera de la función, x =", x)
```

**Tu predicción:**
- Dentro de la función, x = ______
- Fuera de la función, x = ______

> **Nota:** En Python, si quieres modificar una variable global dentro de una función,
> necesitas usar la palabra `global`. Sin embargo, esto se considera **mala práctica**.
> Es mejor pasar variables como parámetros y devolver resultados con `return`.

### Ejercicio 6.11 — Variables globales y locales (II)

Estudia el siguiente código y **sin ejecutarlo**, predice qué se imprime:

```python
contador = 0

def incrementar():
    global contador
    contador += 1

incrementar()
incrementar()
incrementar()
print("Contador:", contador)
```

**Tu predicción:** Contador = ______

> Aquí se usa `global` para modificar la variable del ámbito exterior. Recuerda que
> esto es **mala práctica**. Sería mejor: `contador = incrementar(contador)`.

### Ejercicio 6.12 — Variables globales y locales (III)

Estudia el siguiente código y **sin ejecutarlo**, predice qué se imprime:

```python
def exterior():
    mensaje = "hola"

    def interior():
        print("Interior:", mensaje)

    interior()
    print("Exterior:", mensaje)

exterior()
# print(mensaje)  # ¿Qué pasaría si descomentas esta línea?
```

**Tu predicción:**
- Interior: ______
- Exterior: ______
- Si descomentas `print(mensaje)`: ______

---

## Parte 7: Estructuras de control selectivas

### Teoría

La sintaxis de `if` en Python vs C:

```c
// C
if (edad >= 18) {
    printf("Mayor de edad\n");
} else if (edad >= 13) {
    printf("Adolescente\n");
} else {
    printf("Niño\n");
}
```

```python
# Python
if edad >= 18:
    print("Mayor de edad")
elif edad >= 13:
    print("Adolescente")
else:
    print("Niño")
```

**Diferencias:**
- Sin paréntesis obligatorios en la condición (aunque se pueden usar).
- Dos puntos `:` al final de cada línea `if`, `elif`, `else`.
- `elif` en lugar de `else if`.
- Indentación en lugar de `{}`.

### Ejercicio 7.1 — Replica el ejemplo

Crea un archivo `selectivas.py`:

```python
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
```

### Ejercicio 7.2 — Replica el ejemplo

Escribe y ejecuta el siguiente código que muestra el operador ternario (expresión
condicional) de Python:

```python
# En C:  resultado = (condicion) ? valor_verdadero : valor_falso;
# En Python:
edad = 20
estado = "Mayor" if edad >= 18 else "Menor"
print(estado)   # Mayor

# Otro ejemplo: valor absoluto
n = -7
absoluto = n if n >= 0 else -n
print(f"|{n}| = {absoluto}")   # |-7| = 7

# Útil dentro de print
nota = 8.5
print(f"Resultado: {'Aprobado' if nota >= 6 else 'Reprobado'}")

# Varios valores
hora = 14
saludo = "Buenos días" if hora < 12 else "Buenas tardes" if hora < 20 else "Buenas noches"
print(saludo)   # Buenas tardes
```

> En C: `char *estado = (edad >= 18) ? "Mayor" : "Menor";`

### Ejercicio 7.3 — Replica el ejemplo

Escribe y ejecuta el siguiente código que muestra el uso de condiciones con
operadores lógicos y el operador `in`:

```python
# Verificar rango con comparación encadenada
temp = 25
if 20 <= temp <= 30:
    print("Temperatura agradable")

# Usar "in" para verificar pertenencia
dia = "sábado"
if dia in ("sábado", "domingo"):
    print(f"{dia} es fin de semana")
else:
    print(f"{dia} es día laboral")

# Condiciones múltiples con and/or
edad = 20
tiene_credencial = True
if edad >= 18 and tiene_credencial:
    print("Puede entrar")

# Verificar si una cadena está vacía
nombre = ""
if not nombre:
    print("El nombre está vacío")  # Las cadenas vacías son "falsy"

# Valores "truthy" y "falsy"
# Falsy: 0, 0.0, "", [], {}, (), None, False
# Truthy: todo lo demás
print(bool(0))      # False
print(bool(42))     # True
print(bool(""))     # False
print(bool("hola")) # True
print(bool([]))     # False
print(bool([1]))    # True
```

### Ejercicio 7.4 — Completa el código

Completa la función que clasifica una calificación numérica en letras.

```python
def calificacion_letra(nota):
    if ???:
        return "A"    # 90-100
    elif ???:
        return "B"    # 80-89
    elif ???:
        return "C"    # 70-79
    elif ???:
        return "D"    # 60-69
    else:
        return "F"    # menos de 60

# Pruebas
print(calificacion_letra(95))   # A
print(calificacion_letra(82))   # B
print(calificacion_letra(75))   # C
print(calificacion_letra(61))   # D
print(calificacion_letra(45))   # F
```

### Ejercicio 7.5 — Completa el código

Completa la función que determina si un año es bisiesto:

```python
def es_bisiesto(anio):
    if anio % ??? == 0:
        if anio % ??? == 0:
            if anio % ??? == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Pruebas
print(es_bisiesto(2000))   # True  (divisible entre 400)
print(es_bisiesto(1900))   # False (divisible entre 100 pero no entre 400)
print(es_bisiesto(2024))   # True  (divisible entre 4 pero no entre 100)
print(es_bisiesto(2023))   # False (no divisible entre 4)
```

> **Regla:** Un año es bisiesto si es divisible entre 4, EXCEPTO si es divisible entre 100,
> A MENOS QUE también sea divisible entre 400.

### Ejercicio 7.6 — Completa el código

Completa la función que clasifica un carácter según su tipo:

```python
def clasificar_caracter(c):
    if c.???():        # ¿Es una letra?
        if c.???():    # ¿Es mayúscula?
            return "Letra mayúscula"
        else:
            return "Letra minúscula"
    elif c.???():      # ¿Es un dígito?
        return "Dígito"
    elif c == " ":
        return "Espacio"
    else:
        return "Carácter especial"

# Pruebas
print(clasificar_caracter("A"))   # Letra mayúscula
print(clasificar_caracter("z"))   # Letra minúscula
print(clasificar_caracter("5"))   # Dígito
print(clasificar_caracter(" "))   # Espacio
print(clasificar_caracter("@"))   # Carácter especial
```

> **Pistas:** `isalpha()`, `isupper()`, `isdigit()` son métodos de cadenas.

### Ejercicio 7.7 — Opción múltiple

¿Cuál es el equivalente en Python de la siguiente estructura en C?

```c
switch(opcion) {
    case 1: printf("Uno"); break;
    case 2: printf("Dos"); break;
    default: printf("Otro"); break;
}
```

- a)
    ```python
    switch opcion:
        case 1: print("Uno")
        case 2: print("Dos")
        default: print("Otro")
    ```

- b)
    ```python
    if opcion == 1:
        print("Uno")
    elif opcion == 2:
        print("Dos")
    else:
        print("Otro")
    ```

- c)
    ```python
    match opcion:
        case 1: print("Uno")
        case 2: print("Dos")
        case _: print("Otro")
    ```

- d) Tanto b) como c) son válidas (c a partir de Python 3.10)

**Respuesta:** ______

### Ejercicio 7.8 — Opción múltiple

¿Qué imprime el siguiente código?

```python
x = 0
if x:
    print("verdadero")
else:
    print("falso")
```

- a) `verdadero`
- b) `falso`
- c) Error: `x` no es un booleano
- d) No imprime nada

**Respuesta:** ______

> Recuerda: `0`, `""`, `[]`, `None` y `False` son "falsy" (se evalúan como `False`).

### Ejercicio 7.9 — Opción múltiple

¿Qué imprime el siguiente código?

```python
valor = 15
resultado = "par" if valor % 2 == 0 else "impar"
print(resultado)
```

- a) `par`
- b) `impar`
- c) Error: la sintaxis es inválida
- d) `15`

**Respuesta:** ______

---

## Parte 8: Estructuras de control repetitivas

### Teoría

**Ciclo `while`** — Funciona igual que en C, pero sin `()` ni `{}`:

```c
// C
int i = 0;
while (i < 5) {
    printf("%d\n", i);
    i++;
}
```

```python
# Python
i = 0
while i < 5:
    print(i)
    i += 1     # No existe ++ en Python
```

**Ciclo `for`** — En Python, `for` itera sobre secuencias (listas, cadenas, rangos...),
**no** usa contador como en C:

```c
// C
for (int i = 0; i < 5; i++) {
    printf("%d\n", i);
}
```

```python
# Python
for i in range(5):    # range(5) genera: 0, 1, 2, 3, 4
    print(i)
```

**Iterar sobre una lista directamente** (no se necesita índice):

```python
frutas = ["manzana", "naranja", "plátano"]
for fruta in frutas:
    print(fruta)
```

**Si necesitas el índice Y el valor**, usa `enumerate()`:

```python
for i, fruta in enumerate(frutas):
    print(f"Índice {i}: {fruta}")
```

### Ejercicio 8.1 — Replica el ejemplo

Crea un archivo `ciclos.py`:

```python
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
```

### Ejercicio 8.2 — Replica el ejemplo

Escribe y ejecuta el siguiente código sobre `break`, `continue` y `else` en ciclos:

```python
# break: salir del ciclo prematuramente
print("=== break ===")
for i in range(10):
    if i == 5:
        print("¡Llegué a 5, me detengo!")
        break
    print(i, end=" ")
print()

# continue: saltar a la siguiente iteración
print("\n=== continue ===")
for i in range(10):
    if i % 2 == 0:
        continue    # Salta los pares
    print(i, end=" ")
print()
# Imprime: 1 3 5 7 9

# else en ciclo for (¡no existe en C!)
# El bloque else se ejecuta si el ciclo terminó SIN break
print("\n=== for-else ===")
numeros = [2, 4, 6, 8]
for n in numeros:
    if n % 2 != 0:
        print(f"Encontré un impar: {n}")
        break
else:
    print("Todos los números son pares")
# Imprime: Todos los números son pares
```

> En C, `break` y `continue` funcionan igual. Pero la cláusula `else` en un `for` es exclusiva
> de Python.

### Ejercicio 8.3 — Replica el ejemplo

Escribe y ejecuta el siguiente código sobre ciclos anidados y patrones:

```python
# Ciclos anidados: tabla pitagórica
print("=== Tabla pitagórica (1-5) ===")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:4}", end="")
    print()

# Triángulo de asteriscos
print("\n=== Triángulo ===")
n = 5
for i in range(1, n + 1):
    print("*" * i)

# Triángulo invertido
print("\n=== Triángulo invertido ===")
for i in range(n, 0, -1):
    print("*" * i)

# Iterar sobre dos listas simultáneamente con zip
print("\n=== zip ===")
nombres = ["Ana", "Luis", "María"]
notas = [9.0, 7.5, 8.8]
for nombre, nota in zip(nombres, notas):
    estado = "Aprobado" if nota >= 8 else "Regular"
    print(f"  {nombre}: {nota} ({estado})")
```

### Ejercicio 8.4 — Completa el código

Completa el programa que calcula el factorial de un número usando un ciclo `while`:

```python
def factorial(n):
    resultado = 1
    while ???:
        resultado = resultado * n
        ???
    return resultado

# Pruebas
print("5! =", factorial(5))    # 120
print("0! =", factorial(0))    # 1
print("10! =", factorial(10))  # 3628800
```

### Ejercicio 8.5 — Completa el código

Completa el programa que encuentra los números primos entre 2 y un límite dado:

```python
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, ???):
        if ???:
            return False
    return True

def listar_primos(limite):
    primos = []
    for num in range(2, limite + 1):
        if ???:
            primos.append(num)
    return primos

print(listar_primos(30))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

> **Pista:** Recuerda que para verificar si un número es primo, basta con probar divisores
> hasta la raíz cuadrada del número. En Python puedes usar `int(n**0.5) + 1` como límite.

### Ejercicio 8.6 — Completa el código

Completa el programa que genera la secuencia de Fibonacci hasta un límite:

```python
def fibonacci(limite):
    secuencia = []
    a, b = ???, ???
    while a ???:
        secuencia.append(a)
        a, b = ???, ???
    return secuencia

# Pruebas
print(fibonacci(50))
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

print(fibonacci(100))
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```

> **Pista:** La secuencia empieza con 0 y 1. Cada número es la suma de los dos anteriores.
> La asignación múltiple `a, b = b, a + b` es la forma idiomática en Python.

### Ejercicio 8.7 — Completa el código

Completa un programa que simula un juego de adivinanza:

```python
import random

def juego_adivinanza():
    secreto = random.randint(1, 100)
    intentos = 0

    print("Adivina el número entre 1 y 100")

    while True:
        intento = int(input("Tu intento: "))
        intentos ???= 1

        if intento ???:
            print("¡Correcto! Lo lograste en", intentos, "intentos")
            ???     # terminar el ciclo
        elif intento ??? secreto:
            print("Demasiado bajo")
        else:
            print("Demasiado alto")

juego_adivinanza()
```

### Ejercicio 8.8 — Completa el código

Completa el código que genera todas las combinaciones de dos dados y cuenta cuántas
suman un valor dado:

```python
def contar_sumas(objetivo):
    conteo = 0
    combinaciones = []
    for dado1 in range(???, ???):
        for dado2 in range(???, ???):
            if dado1 + dado2 ???:
                conteo += 1
                combinaciones.append((dado1, dado2))
    return conteo, combinaciones

objetivo = 7
total, combos = contar_sumas(objetivo)
print(f"Formas de obtener {objetivo} con dos dados: {total}")
for c in combos:
    print(f"  {c[0]} + {c[1]} = {objetivo}")
```

**Salida esperada:**
```
Formas de obtener 7 con dos dados: 6
  1 + 6 = 7
  2 + 5 = 7
  3 + 4 = 7
  4 + 3 = 7
  5 + 2 = 7
  6 + 1 = 7
```

### Ejercicio 8.9 — Completa el código

Completa el código que convierte un número decimal a binario usando un ciclo:

```python
def decimal_a_binario(n):
    if n == 0:
        return "0"
    binario = ""
    while ???:
        residuo = n ??? 2
        binario = ???(residuo) + binario
        n = n ??? 2
    return binario

# Pruebas
print(decimal_a_binario(0))    # 0
print(decimal_a_binario(10))   # 1010
print(decimal_a_binario(255))  # 11111111
print(decimal_a_binario(42))   # 101010
```

> **Pista:** Divide entre 2 repetidamente, el residuo (`%`) forma los dígitos binarios de
> derecha a izquierda. Usa `str()` para convertir el residuo a cadena.

### Ejercicio 8.10 — Opción múltiple

¿Qué imprime el siguiente código?

```python
for i in range(2, 10, 3):
    print(i, end=" ")
```

- a) `2 3 4 5 6 7 8 9`
- b) `2 5 8`
- c) `2 4 6 8`
- d) `3 6 9`

**Respuesta:** ______

> **Nota:** `range(inicio, fin, paso)` — similar a `for(int i = inicio; i < fin; i += paso)` en C.

### Ejercicio 8.11 — Opción múltiple

¿Qué imprime el siguiente código?

```python
for i in range(5):
    if i == 3:
        break
    print(i, end=" ")
```

- a) `0 1 2 3`
- b) `0 1 2`
- c) `0 1 2 4`
- d) `3`

**Respuesta:** ______

### Ejercicio 8.12 — Opción múltiple

¿Qué imprime el siguiente código?

```python
for i in range(5):
    if i == 3:
        continue
    print(i, end=" ")
```

- a) `0 1 2 3 4`
- b) `0 1 2`
- c) `0 1 2 4`
- d) `3`

**Respuesta:** ______

---

## Parte 9: Entrada de datos y ejecución desde terminal

### Teoría

En C, para leer datos del usuario usamos `scanf`:

```c
int edad;
printf("¿Cuántos años tienes? ");
scanf("%d", &edad);
```

En Python, usamos `input()`. **Siempre devuelve una cadena**, así que hay que convertir
si necesitamos un número:

```python
edad = int(input("¿Cuántos años tienes? "))
```

### Ejercicio 9.1 — Programa interactivo: Calculadora

Crea un archivo `calculadora.py` que funcione como una calculadora básica interactiva.
Ejecútalo desde la terminal con `python3 calculadora.py`.

```python
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
```

### Ejercicio 9.2 — Programa interactivo: Conversor de unidades

Crea un archivo `conversor.py`. El programa pide al usuario un valor y le permite
elegir el tipo de conversión:

```python
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
```

### Ejercicio 9.3 — Programa interactivo: Encuesta

Crea un archivo `encuesta.py` que recolecte datos de los miembros del equipo y muestre
un resumen:

```python
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
```

---

## Parte 10: Bibliotecas

### Teoría

En C usamos `#include` para incluir bibliotecas:

```c
#include <stdio.h>
#include <math.h>
```

En Python usamos `import`:

```python
import math
from random import randint
```

Python tiene una enorme **biblioteca estándar** y miles de bibliotecas externas. Algunas
bibliotecas populares:

| Biblioteca     | Uso                                    |
|----------------|----------------------------------------|
| `math`         | Funciones matemáticas                  |
| `random`       | Generación de números aleatorios       |
| `os`           | Interacción con el sistema operativo   |
| `sys`          | Parámetros del sistema                 |
| `datetime`     | Manejo de fechas y horas               |

### Ejercicio 10.1 — Replica el ejemplo

Crea un archivo `bibliotecas.py`:

```python
import math
import random

# Biblioteca math
print("=== math ===")
print("Pi:", math.pi)
print("e:", math.e)
print("sqrt(144):", math.sqrt(144))
print("ceil(4.2):", math.ceil(4.2))
print("floor(4.8):", math.floor(4.8))
print("log2(1024):", math.log2(1024))

# Biblioteca random
print("\n=== random ===")
print("Entero aleatorio [1, 10]:", random.randint(1, 10))
print("Flotante aleatorio [0, 1):", random.random())

colores = ["rojo", "verde", "azul", "amarillo"]
print("Elección aleatoria:", random.choice(colores))

random.shuffle(colores)
print("Lista mezclada:", colores)
```

### Ejercicio 10.2 — Replica el ejemplo

Escribe y ejecuta el siguiente código sobre la biblioteca `datetime`:

```python
from datetime import datetime, timedelta

# Fecha y hora actual
ahora = datetime.now()
print("Ahora:", ahora)
print("Año:", ahora.year)
print("Mes:", ahora.month)
print("Día:", ahora.day)
print("Hora:", ahora.hour)

# Formatear fecha (como strftime en C)
print("Formato personalizado:", ahora.strftime("%d/%m/%Y %H:%M"))
# Ejemplo: 17/04/2026 14:30

# Calcular diferencia entre fechas
nacimiento = datetime(2006, 3, 15)
diferencia = ahora - nacimiento
print(f"Días de vida: {diferencia.days}")
print(f"Años aproximados: {diferencia.days // 365}")

# Sumar tiempo
manana = ahora + timedelta(days=1)
print("Mañana:", manana.strftime("%d/%m/%Y"))

proxima_semana = ahora + timedelta(weeks=1)
print("Próxima semana:", proxima_semana.strftime("%d/%m/%Y"))
```

### Ejercicio 10.3 — Replica el ejemplo

Escribe y ejecuta el siguiente código sobre la biblioteca `os` para interactuar con
el sistema de archivos:

```python
import os

# Directorio actual
print("Directorio actual:", os.getcwd())

# Listar archivos en el directorio actual
print("\nArchivos en el directorio:")
for archivo in os.listdir("."):
    tipo = "DIR" if os.path.isdir(archivo) else "FILE"
    print(f"  [{tipo}] {archivo}")

# Verificar si un archivo existe
archivo = "bibliotecas.py"
if os.path.exists(archivo):
    tamano = os.path.getsize(archivo)
    print(f"\n'{archivo}' existe y pesa {tamano} bytes")
else:
    print(f"\n'{archivo}' no existe")

# Variables de entorno
usuario = os.environ.get("USER", "desconocido")
print(f"\nUsuario del sistema: {usuario}")
```

### Ejercicio 10.4 — Completa el código

Completa el siguiente programa que simula el lanzamiento de un dado 1000 veces y
cuenta cuántas veces sale cada cara:

```python
import random

resultados = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for _ in range(1000):
    dado = random.???(1, 6)
    resultados[???] += 1

print("Resultados de 1000 lanzamientos:")
for cara, conteo in resultados.???():
    print(f"  Cara {cara}: {conteo} veces")
```

### Ejercicio 10.5 — Completa el código

Completa el programa que genera contraseñas aleatorias:

```python
import random
import string

def generar_contrasena(longitud=12):
    # string.ascii_letters = 'abcdefg...XYZ'
    # string.digits = '0123456789'
    # string.punctuation = '!@#$%...'
    caracteres = string.ascii_letters + string.??? + string.???
    contrasena = ""
    for _ in range(???):
        contrasena += random.???(caracteres)
    return contrasena

# Generar 5 contraseñas de diferentes longitudes
for longitud in [8, 12, 16, 20, 24]:
    print(f"  Longitud {longitud}: {generar_contrasena(longitud)}")
```

### Ejercicio 10.6 — Completa el código

Completa el programa que usa `math` para calcular la distancia entre dos puntos en el
plano y el área de un triángulo usando la fórmula de Herón:

```python
import math

def distancia(x1, y1, x2, y2):
    return math.???(  (x2-x1)**2 + (???)**2  )

def area_triangulo(x1, y1, x2, y2, x3, y3):
    # Calcular los tres lados
    a = distancia(x1, y1, x2, y2)
    b = distancia(x2, y2, x3, y3)
    c = distancia(x3, y3, x1, y1)

    # Fórmula de Herón: s = semiperímetro
    s = (a + b + c) / ???
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    return area

# Pruebas
print(f"Distancia (0,0)→(3,4): {distancia(0, 0, 3, 4)}")  # 5.0
print(f"Área del triángulo: {area_triangulo(0, 0, 4, 0, 0, 3):.2f}")  # 6.00
```

---

## Parte 11: Ejercicios integradores

Ahora que conoces las bases de Python, es momento de resolver problemas que utilicen
todo lo visto. **Cada miembro del equipo debe encargarse de al menos un ejercicio.**

### Ejercicio integrador A: Gestor de inventario

Crea un archivo `integrador.py`. Desarrolla un programa que administre el inventario de
una tienda. El inventario se representará como una **lista de diccionarios**, donde cada
diccionario es un producto:

```python
{"nombre": "Laptop", "precio": 15000.0, "cantidad": 10}
```

El programa debe mostrar un menú con las siguientes opciones:

1. **Agregar producto** — Pide nombre, precio y cantidad. Agrega el producto al inventario.
2. **Mostrar inventario** — Muestra todos los productos con formato tabular.
3. **Buscar producto** — Pide un nombre y muestra la información del producto si existe.
4. **Actualizar cantidad** — Pide el nombre de un producto y la nueva cantidad.
5. **Eliminar producto** — Pide el nombre y elimina el producto del inventario.
6. **Resumen** — Muestra:
   - Total de productos distintos.
   - Valor total del inventario (suma de precio × cantidad de cada producto).
   - Producto más caro y más barato.
7. **Salir**

**Código base** (completa las funciones en `integrador.py`):

```python
def agregar_producto(inventario):
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    # TODO: Crear el diccionario del producto y agregarlo a la lista
    pass

def mostrar_inventario(inventario):
    if not inventario:
        print("Inventario vacío.")
        return
    print(f"{'Nombre':<20} {'Precio':>10} {'Cantidad':>10}")
    print("-" * 42)
    # TODO: Recorrer el inventario e imprimir cada producto
    pass

def buscar_producto(inventario, nombre):
    # TODO: Buscar y retornar el producto cuyo nombre coincida
    # Retornar None si no se encuentra
    pass

def actualizar_cantidad(inventario):
    nombre = input("Nombre del producto: ")
    producto = buscar_producto(inventario, nombre)
    if producto:
        nueva_cantidad = int(input("Nueva cantidad: "))
        # TODO: Actualizar la cantidad del producto
        pass
    else:
        print("Producto no encontrado.")

def eliminar_producto(inventario):
    nombre = input("Nombre del producto a eliminar: ")
    # TODO: Buscar el producto y eliminarlo de la lista
    # Pista: usa inventario.remove(producto)
    pass

def resumen(inventario):
    if not inventario:
        print("Inventario vacío.")
        return
    # TODO: Calcular e imprimir:
    # - Total de productos distintos
    # - Valor total (sum de precio * cantidad)
    # - Producto más caro y más barato
    pass

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
```

### Ejercicio integrador B: Agenda de contactos

Crea un archivo `agenda.py`. Desarrolla una agenda telefónica que almacene contactos
como diccionarios con llaves `nombre`, `telefono`, `email`. Implementa:

1. **Agregar contacto**
2. **Listar contactos** — Ordenados alfabéticamente por nombre
3. **Buscar contacto** — Búsqueda parcial (que el nombre contenga la cadena buscada)
4. **Editar contacto** — Permite cambiar teléfono o email
5. **Eliminar contacto**
6. **Exportar** — Imprime todos los contactos en formato CSV (separados por comas)
7. **Estadísticas** — Total de contactos, dominios de email más comunes
8. **Salir**

**Código base:**

```python
def agregar_contacto(agenda):
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    # TODO: Crear diccionario y agregarlo a la agenda
    pass

def listar_contactos(agenda):
    if not agenda:
        print("Agenda vacía.")
        return
    # TODO: Ordenar por nombre e imprimir en formato tabular
    # Pista: sorted(agenda, key=lambda c: c["nombre"])
    pass

def buscar_contacto(agenda, termino):
    # TODO: Retornar lista de contactos cuyo nombre contenga 'termino'
    # Pista: usa 'termino.lower() in contacto["nombre"].lower()'
    pass

def editar_contacto(agenda):
    nombre = input("Nombre del contacto a editar: ")
    resultados = buscar_contacto(agenda, nombre)
    if not resultados:
        print("No se encontró el contacto.")
        return
    # TODO: Si hay múltiples resultados, mostrarlos y pedir selección
    # TODO: Pedir nuevo teléfono y/o email (enter para no cambiar)
    pass

def eliminar_contacto(agenda):
    nombre = input("Nombre del contacto a eliminar: ")
    # TODO: Buscar y eliminar
    pass

def exportar_csv(agenda):
    # TODO: Imprimir cada contacto como: nombre,telefono,email
    print("nombre,telefono,email")
    pass

def estadisticas(agenda):
    # TODO: Total de contactos
    # TODO: Contar dominios de email (parte después del @)
    pass

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
```

### Ejercicio integrador C: Análisis de texto

Crea un archivo `analizador.py`. Desarrolla un programa que analice un texto introducido
por el usuario (o un texto predefinido) y muestre estadísticas detalladas.

**Funciones a implementar:**

```python
def contar_palabras(texto):
    # TODO: Retornar el número total de palabras
    pass

def contar_oraciones(texto):
    # TODO: Contar oraciones (terminan en '.', '!' o '?')
    pass

def palabra_mas_frecuente(texto):
    # TODO: Retornar la palabra que más se repite (ignorar mayúsculas)
    # Pista: usa un diccionario para contar frecuencias
    pass

def palabras_unicas(texto):
    # TODO: Retornar un conjunto (set) de palabras únicas
    pass

def longitud_promedio_palabras(texto):
    # TODO: Retornar la longitud promedio de las palabras
    pass

def buscar_palabra(texto, palabra):
    # TODO: Retornar cuántas veces aparece la palabra en el texto
    pass

def reemplazar_palabra(texto, vieja, nueva):
    # TODO: Retornar el texto con la palabra vieja reemplazada por la nueva
    pass

# Texto de ejemplo para analizar
texto_ejemplo = """
Python es un lenguaje de programación muy popular. Python es fácil de aprender.
Muchos programadores usan Python para ciencia de datos y para desarrollo web.
Python tiene una gran comunidad. La comunidad de Python es muy activa y amigable.
¿Te gusta programar? ¡Python es una excelente opción para empezar!
"""

print("=== ANALIZADOR DE TEXTO ===")
print(f"Total de palabras: {contar_palabras(texto_ejemplo)}")
print(f"Total de oraciones: {contar_oraciones(texto_ejemplo)}")
print(f"Palabra más frecuente: {palabra_mas_frecuente(texto_ejemplo)}")
print(f"Palabras únicas: {len(palabras_unicas(texto_ejemplo))}")
print(f"Longitud promedio: {longitud_promedio_palabras(texto_ejemplo):.1f}")
print(f"Veces que aparece 'Python': {buscar_palabra(texto_ejemplo, 'Python')}")

nuevo = reemplazar_palabra(texto_ejemplo, "Python", "Java")
print(f"\nTexto modificado (primeras 100 letras):\n{nuevo[:100]}...")
```

---

## Tabla resumen: C vs Python

| Concepto               | C                                     | Python                                  |
|------------------------|---------------------------------------|-----------------------------------------|
| Declarar variable      | `int x = 5;`                          | `x = 5`                                 |
| Imprimir               | `printf("Hola %s\n", nombre);`        | `print(f"Hola {nombre}")`               |
| Leer entrada           | `scanf("%d", &x);`                    | `x = int(input("valor: "))`             |
| Arreglo/Lista          | `int arr[5] = {1,2,3,4,5};`          | `arr = [1, 2, 3, 4, 5]`                |
| Tamaño de arreglo      | No integrado (usar `sizeof`)          | `len(arr)`                              |
| Cadena                 | `char s[] = "hola";`                  | `s = "hola"`                            |
| Función                | `int f(int a) { return a; }`          | `def f(a): return a`                    |
| if-else                | `if (x > 0) {...} else {...}`         | `if x > 0: ... else: ...`              |
| for                    | `for(int i=0; i<n; i++){...}`         | `for i in range(n): ...`               |
| while                  | `while(cond) {...}`                   | `while cond: ...`                       |
| Incluir biblioteca     | `#include <math.h>`                   | `import math`                           |
| Punto y coma           | Obligatorio `;`                       | No se usa                               |
| Llaves `{}`            | Delimitan bloques                     | Se usa indentación                      |
| Tipado                 | Estático                              | Dinámico                                |

---

## Respuestas a los ejercicios de opción múltiple

*(Recortar esta sección si se entrega a los alumnos)*

| Ejercicio | Respuesta | Explicación breve |
|-----------|-----------|-------------------|
| 1.4       | c)        | En Python no se declara el tipo antes de la variable. |
| 1.5       | b)        | Python tiene tipado dinámico; al reasignar `"diez"`, `x` es `str`. |
| 1.6       | c)        | `int()` no puede convertir `"3.14"` directamente; lanza `ValueError`. |
| 1.7       | b)        | Al sumar `int` + `float`, Python promueve el resultado a `float`. |
| 1.8       | c)        | `lambda` es palabra reservada de Python. `main`, `printf`, `include` no lo son. |
| 1.9       | b)        | `a, b = b, a` intercambia los valores: `a=10, b=5`. |
| 2.7       | b)        | Las cadenas son inmutables; la asignación por índice lanza `TypeError`. |
| 2.8       | c)        | `split()` sin argumentos divide por espacios y devuelve una lista. |
| 2.9       | b)        | `s[-1]` es el último carácter (`n`), `s[-2]` es el penúltimo (`o`). |
| 3.4       | b)        | `7/2 = 3.5`, `7//2 = 3` (int), `7%2 = 1` (int). |
| 3.5       | b)        | `2 ** 10 = 1024`. El operador `**` es potencia. |
| 3.6       | b)        | `x=10`, `x+=5→15`, `x*=2→30`. |
| 3.7       | c)        | `++` no existe en Python. Se usa `+= 1`. |
| 3.8       | b)        | `10 == 10.0` es `True` (mismo valor), `10 is 10.0` es `False` (distintos objetos). |
| 3.9       | a)        | Python admite comparaciones encadenadas: `5 < 10 < 20` y `5 < 10 > 3` ambas `True`. |
| 4.7       | b)        | `lista[1:3]` toma índices 1 y 2 → `[2, 3]`. |
| 4.8       | b)        | `append` agrega `[40, 50]` como un solo elemento → longitud 4. |
| 4.9       | b)        | `b = a` no copia la lista; ambas variables apuntan al mismo objeto. |
| 4.10      | c)        | `range(5)` genera 0..4; multiplicado por 2 da `[0, 2, 4, 6, 8]`. |
| 4.11      | b)        | `lista[-2]` es el penúltimo elemento → `4`. |
| 4.12      | a)        | `sort()` ordena in-place, `reverse()` invierte in-place. |
| 5.7       | b)        | Las listas son mutables; las tuplas no. |
| 5.8       | b)        | Se actualiza el valor de la llave `"b"` a 20. |
| 5.9       | b)        | `get("z", 0)` retorna `0` cuando la llave no existe. |
| 5.10      | b)        | `list(tupla)` crea una lista independiente; la tupla original no cambia. |
| 5.11      | a)        | `len(d)` cuenta el número de llaves = 3. |
| 5.12      | d)        | Las listas son mutables y no pueden ser llaves de diccionario. |
| 7.7       | d)        | `if/elif/else` funciona siempre; `match/case` desde Python 3.10. |
| 7.8       | b)        | `0` es "falsy", así que se ejecuta el `else`. |
| 7.9       | b)        | `15 % 2 == 0` es `False`, así que el resultado es `"impar"`. |
| 8.10      | b)        | `range(2, 10, 3)` → 2, 5, 8. |
| 8.11      | b)        | `break` sale del ciclo cuando `i == 3`, antes de imprimirlo. |
| 8.12      | c)        | `continue` salta la impresión cuando `i == 3`, pero continúa con 4. |

---

## Referencias

- Documentación oficial de Python: https://docs.python.org/3/
- Tipos de datos y operadores: https://docs.python.org/3/library/stdtypes.html
- Métodos de cadenas: https://docs.python.org/3/library/stdtypes.html#string-methods
- Listas: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
- Diccionarios: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
- Biblioteca estándar: https://docs.python.org/3/library/
