
#41. Leer 10 números enteros, almacenarlos en un vector y determinar cuántos números de los
# almacenados en dicho vector comienzan con 3.
vector = []
contador = 0
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    while number >= 10:
        number = int(number / 10)
    if number == 3:
        contador = contador + 1
print("Cantidad de números que comienzan con 3: " + str(contador))

#42. Leer 10 números enteros, almacenarlos en un vector y determinar cuántos números con
# cantidad par de dígitos pares hay almacenados en dicho vector.
vector = []
pares = []
contador = 0
two = 0
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    two = 0
    while number >= 1:
        unidad = int(number % 10)
        if int(unidad % 2) == 0:
            two = two + 1
        number = int(number / 10)
    pares.append(two)
for par in pares:
    if int(par % 2) == 0:
        contador = contador + 1
print("Cantidad de números con cantidad par de dígitos pares: " + str(contador))

#43. Leer 10 números enteros, almacenarlos en un vector y determinar en qué posiciones se
# encuentra el número con mayor cantidad de dígitos primos.
vector = []
contador = 0
primos = []
donde = 0
posiciones = []
primo = False
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    contador = 0
    while number >= 1:
        unidad = int(number % 10)
        number = int(number / 10)
        for x in range(2, (unidad - 1)):
            if int(unidad % x) == 0:
                primo = False
                break
            primo = True
        if primo == True or unidad == 2 or unidad == 3:
            contador = contador + 1
    primos.append(contador)
mayor = primos[0]
for prim in primos:
    if prim > mayor:
        mayor = prim
for number in primos:
    donde = donde + 1
    if number == mayor:
        posiciones.append(donde)
print("Posiciones donde se encuentra el número con mayor cantidad de dígitos primos: " str(posiciones))  

#44. Leer 10 números enteros, almacenarlos en un vector y determinar cuántos de los números
# almacenados en dicho vector pertenecen a los 100 primeros elementos de la serie de
# Fibonacci.
fibonacci = []
vector = []
contador = 0
x = 0
y = 1
for number in range(0, 50):
    fibonacci.append(x)
    fibonacci.append(y)
    x = x + y
    y = x + y
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for num in vector:
    for dato in fibonacci:
        if num == dato:
            contador = contador + 1
print("Cantidad de números que aparecen en los 100 primeros numeros de la lista de Fibonacci son: " + str(contador))

#45. Leer 10 números enteros, almacenarlos en un vector y determinar cuántos números de los
# almacenados en dicho vector comienzan por 34.
vector = []
contador = 0
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    while number >= 100:
        number = int(number / 10)
    if number == 34:
        contador = contador + 1
print("Cantidad de números que comienzan con 3: " + str(contador))

#46. Leer 10 números enteros, almacenarlos en un vector y determinar cuántos números de los
# almacenados en dicho vector son primos y comienzan por 5.
vector = []
contador = 0
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    for x in range(2, (number - 1)):
        if int(number % x) == 0:
            is_prime = False
            break
        is_prime = True
    while number >= 10:
        number = int(number / 10)   
    if is_prime == True and number == 5:
        contador = contador + 1

print("Cantidad de números que comienzan con 3: " + str(contador))

#47. Leer 10 números enteros, almacenarlos en un vector y determinar en qué posiciones se
# encuentran los números múltiplos de 10. No utilizar el número 10 en ninguna operación.
vector = []
contador = 0
tens = []
posiciones = []
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    if int(number % 5) == 0 and int(number % 2) == 0:
        tens.append(number)
for number in vector:
    contador = contador + 1
    for ten in tens:
        if number == ten:
            posiciones.append(contador)
            break
print("Número múltiplos de diez: " + str(tens))
print("Posiciones en las que hay un múltiplo de diez: " + str(posiciones))

#48. Leer 10 números enteros, almacenarlos en un vector y determinar en qué posición se
# encuentra el número primo con mayor cantidad de dígitos pares.
vector = []
primos = []
pares = []
posiciones = []
contador = 0
mayor = 0
is_prime = False
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    for x in range(2, (number - 1)):
        if int(number % x) == 0:
            is_prime = False
            primos.append(0)
            break
        is_prime = True
    if is_prime == True or number == 2 or number == 3:
        primos.append(number)
for primo in primos:
    two = 0
    while primo >= 1:
        unidad = int(primo % 10)
        if int(unidad % 2) == 0:
            two = two + 1
        primo = int(primo / 10)
    pares.append(two)
mayor = pares[0]
for par in pares:
    contador = contador + 1
    if par > mayor and int(par % 2) == 0:
        posiciones.append(contador)
print("Posiciones de los números primos con mayor cantidad de dígitos primos: " + str(posiciones))

#49. Leer 10 números enteros, almacenarlos en un vector y determinar cuántos números terminar
# en dígito primo.
vector = []
contador = 0
is_prime = False
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    unidad = int(number % 10)
    for x in range(2, (unidad - 1)):
        if int(unidad % x) == 0:
            is_prime = False
            break
        is_prime = True   
    if is_prime == True or unidad == 2 or unidad == 3:
        contador = contador + 1
        print(unidad)
print("Cantidad de números que terminan en dígito primo: " + str(contador))  

#50. Leer 10 números enteros, almacenarlos en un vector y determinar cuántos números de los
# almacenados en dicho vector comienzan en dígito primo.
vector = []
contador = 0
primeros = []
is_prime = False
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    while number >= 10:
        number = int(number / 10)
    primeros.append(number)
for primero in primeros:
    for x in range(2, (primero - 1)):
        if int(primero % x) == 0:
            is_prime = False
            break
        is_prime = True   
    if is_prime == True or primero == 2 or primero == 3:
        contador = contador + 1
print("Cantidad de números que comienzan con un número primo: " + str(contador))
