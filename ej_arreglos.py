
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
