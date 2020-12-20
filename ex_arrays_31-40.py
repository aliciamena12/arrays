
#31. Leer 10 números enteros, almacenarlos en un vector. Luego leer un entero y determinar
# cuantos divisores exactos tiene este último número entre los valores almacenados en el vector.
vector = []
contador = 0
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
num = int(input("Elige otro número entero para comparar: "))
for number in vector:
    if int(num % number) == 0:
        contador = contador + 1
print("Cantidad de divisores exactos que tiene el último número entre los almacenados: " + str(contador))

#32. Leer 10 números enteros, almacenarlos en un vector. Luego leer un entero y determinar
# cuántos números de los almacenados en el vector terminan en el mismo dígito que el último
# valor leído.
vector = []
x = 0
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
num = int(input("Elige un número para comparar: "))
ultimo = int(num % 10)
for number in vector:
    unidad = int(number % 10)
    if unidad == ultimo:
        x = x + 1
print("El número elegido coincide en el último digito con " + str(x) + " números almacenados.")

#33. Leer 10 números enteros, almacenarlos en un vector y determinar a cuánto es igual la suma de
# los dígitos pares de cada uno de los números leídos.
vector = []
suma = 0
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    while number >= 1:
        unidad = int(number % 10)
        if int(unidad % 2) == 0:
            suma = suma + unidad
        number = int(number / 10)

print("La suma de los dígitos pares de los números es: " + str(suma))

#34. Leer 10 números enteros, almacenarlos en un vector y determinar cuántas veces en el vector
# se encuentra el dígito 2. No se olvide que el dígito 2 puede estar varias veces en un mismo
# número.
vector = []
two = 0
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    while number >= 1:
        unidad = int(number % 10)
        if unidad == 2:
            two = two + 1
        number = int(number / 10)

print("Cantidad de dígito 2: " + str(two))

#35. Leer 10 números enteros, almacenarlos en un vector y determinar si el promedio entero de
# dichos números es un número primo.
vector = []
suma = 0
contador = 0
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    suma = suma + number
    contador = contador + 1
promedio = int(suma / contador)
for x in range(2, (promedio-1)):
    if int(promedio % x) == 0:
        primo = False
        break
    primo = True
if primo == True:
    print("El promedio entero de los números elegidos es un número primo.")
else:
    print("El promedio entero de los números elegidos no es un número primo.")

#36. Leer 10 números enteros, almacenarlos en un vector y determinar cuántos dígitos primos hay
# en los números leídos.
vector = []
contador = 0
primo = False
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
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

print("Cantidad de dígito primos: " + str(contador))

#37. Leer 10 números enteros, almacenarlos en un vector y determinar a cuántos es igual el
# cuadrado de cada uno de los números leídos.
vector = []
cuadrados = []
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    cuadrados.append(number * number)
print(cuadrados)

#38. Leer 10 números enteros, almacenarlos en un vector y determinar si la semisuma entre el valor
# mayor y el valor menor es un número primo.
vector = []
mayor = 0
menor = 0
primo = False
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
mayor = vector[0]
for number in vector:
    if number > mayor:
        mayor = number
menor = vector[0]
for number in vector:
    if number < menor:
        menor = number
semisuma = int((mayor + menor) / 2)
for x in range(2, (semisuma - 1)):
    if int(semisuma % x) == 0:
        primo = False
        break
    primo = True
if primo == True or semisuma == 2 or semisuma == 3:
    print("La semisuma entre el mayor valor y el menor es un número primo.")
else:
    print("La semisuma entre el mayor valor y el menor no es un número primo.")

#39. Leer 10 números enteros, almacenarlos en un vector y determinar si la semisuma entre el valor
# mayor y el valor menor es un número par.
vector = []
mayor = 0
menor = 0
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
mayor = vector[0]
for number in vector:
    if number > mayor:
        mayor = number
menor = vector[0]
for number in vector:
    if number < menor:
        menor = number
semisuma = int((mayor + menor) / 2)
if int(semisuma % 2) == 0:
    print("La semisuma entre el mayor valor y el menor es un número par.")
else:
    print("La semisuma entre el mayor valor y el menor no es un número par.")

#40. Leer 10 números enteros, almacenarlos en un vector y determinar cuántos números de los
# almacenados en dicho vector terminan en 15.
vector = []
contador = 0
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    final = int(number % 100)
    if final == 15:
        contador = contador + 1
print("Cantidad de números que acaban en 15: " + str(contador))
