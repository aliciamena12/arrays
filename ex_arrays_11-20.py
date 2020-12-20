
#11. Leer 10 números enteros, almacenarlos en un vector y determinar cuántos números tienen, de
# los almacenados allí, tienen menos de 3 dígitos.
vector = []
contador = 0
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    if number < 100:
        contador = contador + 1
print("Cantidad de números con menos de 3 dígitos: " + str(contador))

#12. Leer 10 números enteros, almacenarlos en un vector y determinar a cuánto es igual el
# promedio entero de los datos del vector.
vector = []
suma = 0
contador = 0
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    suma = suma + number
    contador = contador + 1
promedio = int(suma / contador)
print("El promedio entero de los números elegidos es: " + str(promedio))

#13. Leer 10 números enteros, almacenarlos en un vector y determinar si el promedio entero de
# estos datos está almacenado en el vector.
vector = []
suma = 0
contador = 0
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    suma = suma + number
    contador = contador + 1
promedio = int(suma / contador)
for number in vector:
    if number == promedio:
        print("El promedio entero de los números elegidos es uno de los números.")
        break
else:
    print("El promedio entero de los números elegidos no es uno de los números.") 

#14. Leer 10 números enteros, almacenarlos en un vector y determinar cuántas veces se repite el
# promedio entero de los datos dentro del vector.
vector = []
suma = 0
contador = 0
repetido = 0
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    suma = suma + number
    contador = contador + 1
promedio = int(suma / contador)
for number in vector:
    if number == promedio:
        repetido = repetido + 1
print("En la lista hay " + str(repetido) + " números que coinciden con el promedio entero de los números elegidos.")

#15. Leer 10 números enteros, almacenarlos en un vector y determinar cuántos datos almacenados
# son múltiplos de 3.
vector = []
contador = 0
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    if int(number % 3) == 0:
        contador = contador + 1
print("En la lista hay " + str(contador) + " números múltiplos de 3.")

#16. Leer 10 números enteros, almacenarlos en un vector y determinar cuáles son los datos
# almacenados múltiplos de 3.
vector = []
multiplos = []
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    if int(number % 3) == 0:
        multiplos.append(number)
print("Los números múltiplos de 3 son: " + str(multiplos))

#17. Leer 10 números enteros, almacenarlos en un vector y determinar cuántos números negativos
# hay.
vector = []
contador = 0
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    if number < 0:
        contador = contador + 1
print("En la lista hay " + str(contador) + " números negativos.")

#18. Leer 10 números enteros, almacenarlos en un vector y determinar en qué posiciones están los
# números positivos.
vector = []
contador = 0
positivos = []
posiciones = []
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
for number in vector:
    if number > 0:
        positivos.append(number)
for number in vector:
    contador = contador + 1
    for positivo in positivos:
        if number == positivo:
            posiciones.append(contador)
            break
print("Posiciones en las que hay números positivos: " + str(posiciones))

#19. Leer 10 números enteros, almacenarlos en un vector y determinar cuál es el número menor.
vector = []
x = 0
for i in range(0, 10):
    vector.append(int(input("Elige un número entero: ")))
x = vector[0]
for number in vector:
    if number < x:
        x = number
print("El número más pequeño es: " + str(x))

#20. Leer 10 números enteros, almacenarlos en un vector y determinar en qué posición está el
# menor número primo.
vector = []
primos = []
x = 0 
menor = 0
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
menor = primos[0]
for primo in primos:
    if primo < menor:
        menor = primo
for number in vector:
    contador = contador + 1
    if number == menor:
        break 
print("El número primo más pequeño esta en la posición: " + str(contador))
