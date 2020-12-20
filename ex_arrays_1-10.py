
#1. Leer 10 enteros, almacenarlos en un vector y determinar en qué posición del vector está el
# mayor número leído.
vector = []
grande = 0
contador = 1
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    if number > grande:
        grande = number
for number in vector:
    if number == grande:
        break
    else:
        contador = contador + 1
print("El mayor número esta en la posición: " + str(contador))

#2. Leer 10 enteros, almacenarlos en un vector y determinar en qué posición del vector está el
# mayor número par leído.
vector = []
grande = 0
contador = 1
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    if number > grande and int(number % 2) == 0:
        grande = number
for number in vector:
    if number == grande:
        break
    else:
        contador = contador + 1
print("El mayor número par esta en la posición: " + str(contador))

#3. Leer 10 enteros, almacenarlos en un vector y determinar en qué posición del vector está el
#mayor número primo leído.
vector = []
primos = []
x = 0 
mayor = 0
contador = 0
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    for x in range(2, (number - 1)):
        if int(number % x) == 0:
            is_prime = False
            break
        is_prime = True
    if is_prime == True:
        primos.append(number)
print(primos)
mayor = primos[0]
for primo in primos:
    if primo > mayor:
        mayor = primo
for number in vector:
    contador = contador + 1
    if number == mayor:
        break 
print("El número primo más grande esta en la posicion: " + str(contador))

#4. Cargar un vector de 10 posiciones con los 10 primeros elementos de la serie de Fibonacci y
# mostrarlo en pantalla.
vector = []
x = 0
y = 1
for number in range(0, 5):
    vector.append(x)
    vector.append(y)
    x = x + y
    y = x + y
print(vector)

#5. Almacenar en un vector de 10 posiciones los 10 números primos comprendidos entre 100 y
# 300. Luego mostrarlos en pantalla.
vector = []
primos = []
x = 0 
for number in range(100, 300):
    for x in range(2, (number - 1)):
        if int(number % x) == 0:
            is_prime = False
            break
        is_prime = True
    if is_prime == True:
        for i in range(0, 10):
            vector.append(number)
            break
for num in vector[:10]:
    primos.append(num)
print(primos)

#6. Leer dos números enteros y almacenar en un vector los 10 primeros números primos
# comprendidos entre el menor y el mayor. Luego mostrarlos en pantalla.
vector = []
num1 = int(input("Elige un número entero: "))
num2 = int(input("Elige un segundo número entero: "))
primos = []
if num1 < num2:
    for number in range(num1, num2):
        for x in range(2, (number - 1)):
            if int(number % x) == 0:
                is_prime = False
                break
            is_prime = True
        if is_prime == True:
            vector.append(number)
elif num2 < num1:
    for number in range(num2, num1):
        for x in range(2, (number - 1)):
            if int(number % x) == 0:
                is_prime = False
                break
            is_prime = True
        if is_prime == True:
            vector.append(number)
else:
    print("Los dos números elegidos son iguales.")
for number in vector[:10]:
    primos.append(number)
print(primos)

#7. Leer 10 números enteros, almacenarlos en un vector y determinar en qué posiciones se
# encuentra el número mayor.
vector = []
contador = 0
mayor = 0
posiciones = []
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
mayor = vector[0]
for number in vector:
    if number > mayor:
        mayor = number
for number in vector:
    contador = contador + 1
    if number == mayor:
        posiciones.append(contador)
print("Posiciones en las que se encuentran el número más grande: " + str(posiciones))

#8. Leer 10 números enteros, almacenarlos en un vector y determinar en qué posiciones se
# encuentran los números terminados en 4.
vector = []
contador = 0
cuatros = []
posiciones = []
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    if int(number % 10) == 4:
        cuatros.append(number)
for number in vector:
    contador = contador + 1
    for cuatro in cuatros:
        if number == cuatro:
            posiciones.append(contador)
            break
print("Posiciones en las que se encuentran los números terminados en 4: " + str(posiciones))

#9. Leer 10 números enteros, almacenarlos en un vector y determinar cuántas veces está repetido
# el mayor.
vector = []
grande = 0
contador = 0
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    if number > grande:
        grande = number
for number in vector:
    if number == grande:
        contador = contador + 1
print("El número más grande está repetido " + str(contador) + " veces.")

#10. Leer 10 números enteros, almacenarlos en un vector y determinar en qué posiciones se
# encuentran los números con mas de 3 dígitos.
vector = []
contador = 0
largos = []
posiciones = []
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    if number >= 1000:
        largos.append(number)
for number in vector:
    contador = contador + 1
    for largo in largos:
        if number == largo:
            posiciones.append(contador)
            break
print("Posiciones en las que se encuentran los números de mas de 3 dígitos: " + str(posiciones))

