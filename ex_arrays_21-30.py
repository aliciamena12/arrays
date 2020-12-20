
#21. Leer 10 números enteros, almacenarlos en un vector y determinar en qué posición está el
# número cuya suma de dígitos sea la mayor.
vector = []
sumas = []
contador = 0
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    suma = 0
    while number >= 1:
        unidad = int(number % 10)
        number = int(number / 10)
        suma = suma + unidad
    sumas.append(suma)
mayor = sumas[0]
for number in sumas:
    if number > mayor:
        mayor = number
for num in sumas:
    contador = contador + 1     
    if num == mayor:
        break 
print("Posición del número cuya suma de dígitos es la mayor es: " + str(contador))

#22. Leer 10 números enteros, almacenarlos en un vector y determinar cuáles son los números
# múltiplos de 5 y en qué posiciones están.
vector = []
contador = 0
cincos = []
posiciones = []
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    if int(number % 5) == 0:
        cincos.append(number)
for number in vector:
    contador = contador + 1
    for cinco in cincos:
        if number == cinco:
            posiciones.append(contador)
            break
print("Número múltiplos de cinco: " + str(cincos))
print("Posiciones en las que hay un múltiplo de cinco: " + str(posiciones))

#23. Leer 10 números enteros, almacenarlos en un vector y determinar si existe al menos un
# número repetido.
vector = []
contador = 0
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    contador = 0
    for x in vector:
        if x == number:
            contador = contador + 1
    if contador > 1:
        print("Al menos hay un número repetido.")
        contador = 22
        break
if contador != 22:
    print("No hay ningun número repetido.")

#24. Leer 10 números enteros, almacenarlos en un vector y determinar en qué posición está el
# número con mas dígitos.
vector = []
numdig = []
mayor = 0
posicion = 1
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    contador = 0
    while number > 0:
        number = int(number / 10)
        contador = contador + 1
    numdig.append(contador)
print(numdig)
mayor = numdig[0]
for num in numdig:
    if num > mayor:
        mayor = num
for num in numdig:
    if num == mayor:
        break
    posicion = posicion + 1
print("El número con más dígitos esta en la posición: " + str(posicion))

#25. Leer 10 números enteros, almacenarlos en un vector y determinar cuántos de los números
# leídos son números primos terminados en 3.
vector = []
primos3 = []
contador = 0
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    unidad = int(number % 10)
    for x in range((number - 1), 2, -1):
        if int(number % x) == 0:
            is_prime = False
            break
        is_prime = True
    if is_prime == True and unidad == 3:
        contador = contador + 1
print("Números primos terminados en 3: " + str(contador))

#26. Leer 10 números enteros, almacenarlos en un vector y calcularle el factorial a cada uno de los
# números leídos almacenándolos en otro vector.
vector = []
vecfac = []
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    factorial = 1
    for x in range(1, (number + 1)):
        factorial = factorial * x
    vecfac.append(int(factorial))
print("Vector de factoriales:" + str(vecfac))

#27. Leer 10 números enteros, almacenarlos en un vector y determinar a cuánto es igual el
# promedio entero de los factoriales de cada uno de los números leídos.
vector = []
suma = 0
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    factorial = 1
    for x in range(1, (number + 1)):
        factorial = factorial * x
    suma = suma + factorial
    promedio = int(suma / 10)

print("Promedio de los factoriales: " + str(promedio))

#28. Leer 10 números enteros, almacenarlos en un vector y mostrar en pantalla todos los enteros
# comprendidos entre 1 y cada uno de los números almacenados en el vector.
vector = []
suma = 0
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    for x in range(1, (number + 1)):
        print(x)

#29. Leer 10 números enteros, almacenarlos en un vector y mostrar en pantalla todos los enteros
# comprendidos entre 1 y cada uno de los dígitos de cada uno de los números almacenados en
# el vector.
vector = []
digitos = []
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    while number >= 1:
        digito = int(number % 10)
        for x in range(1, (digito + 1)):
            digitos.append(x)
        number = int(number / 10)      
print(digitos)

#30. Leer 10 números enteros, almacenarlos en un vector. Luego leer un entero y determinar si este
# último entero se encuentra entre los 10 valores almacenados en el vector.
vector = []
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
num = int(input("Elige un número para comparar: "))
for number in vector:
    if num == number:
        print("El número elegido coincide con uno de los números almacenados.")
        break
else:
    print("El número elegido no coincide con ninguno de los números almacenados.")
