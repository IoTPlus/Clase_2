#SEGUNDA CLASE

#1 Que hace el siguiente codigo? R: Factorial hasta n
num = int(input("Ingrese numero: "))
nacum = num
i=1
while i<num:
    nacum = nacum * i
    i+=1

print(nacum)

#2 Calcule un programa que calcula promedio de un curso con n alumnos:
num = int(input("Ingrese numero de alumnos en el curso: "))
i = 1
nacum = 0
while i<=num:
    nacum = nacum + float(input(f"Ingrese nota del alumno {i}: "))
    i+=1

prom = nacum/num
print(f"El promedio del curso de {num} alumnos es: {prom}")

#3 Promedio final del curso hasta que se ingrese nota -1
qa=0
nacum = 0
while True:
    nota = int(input("Ingrese nota de alumno: "))
    if nota != -1:
        nacum += nota
        qa+=1
    else:
        break

prom = (nacum/qa)
print(f"Se  ingresaron {qa} notas y el promedio es : {prom}")

#4 Sumatoria de numeros enteros al cuadrado hasta n
num = int(input("Ingrese numero: "))
nacum = 0
i=1
while i<=num:
    nacum = nacum + pow(i,2)
    i+=1

print(nacum)

#5 Factorial
num = int(input("Ingrese numero: "))
fact = 1
i=1
while i<=num:
    fact = fact * i
    i+=1

print(fact)

#5 Contar cantidad de impares ingresados:
num = int(input("Ingrese la cantidad de numeros: "))
i=1
num_impares=0
while i<=num:
    if int(input("Ingrese numero: "))//2 != 0:
        num_impares+=1
    i+=1

print(f"Cantidad de impares ingresados es: {num_impares}")

#6 Tabla de multiplicar hasta el numero ingresado:
num = int(input("Ingrese un numero: "))
i=1
while i <= num:
    print(f"{num} x 1 = {num*i}")

#7 Todos los divisores del numero entregado:
while True:
    num = int(input("Ingrese un numero: "))
    if num <= 0:
        print("Ingrese un numero positivo entero")
    else:
        i = 1
        while i <= num:
            if num % i == 0:
                print(i)
            i += 1
        break

#8 Si numero ingresado es primo o no
num = int(input("Ingrese un número: "))
i = 1
num_divisores = 0
while i <= num:
    if num % i == 0:
        num_divisores += 1
    i+=1

if num_divisores == 2 or num_divisores == 1:
    print(f"{num} es un número primo.")
else:
    print(f"{num} no es número primo.")

#9 Sumar duración de tramos:
total = 0
while True:
    tramo = int(input("Duración tramo: "))
    if tramo != 0:
        total = total + tramo
    else:
        horas = total//60
        minutos = total%60
        print(f"La duración total del viaje fué: {horas}:{minutos} horas")
        break

#10 Sucesión
num = int(input("Ingrese numero:"))
while num != 1:
    if num%2 == 0:
        num = num/2
        print(num)
    else:
        num = num*3 + 1
        print(num)

#11 Encontrar numero mayor
cant = int(input("Ingrese cantidad de numeros: "))
i=1
mayor = 0
while i <= cant:
    num = int(input("Ingrese numero: "))
    if num > mayor:
        mayor = num
    i+=1

print(f"El numero mayor es: {mayor}")

#12 Encuentro el menor numero
i=1
cant = int(input("Ingrese cantidad de numeros: "))
menor = int(input("Ingrese  numero: "))
while i < cant:
    num = int(input("Ingrese numero: "))
    if num < menor:
        menor = num
    i+=1

print(f"El numero menor es: {menor}")

#13 Combinacion de dados cuya suma sea mayor a 7
i=1
j=1
combinación=1
while i<=6:
    while j<=6:
        if i+j > 7:
            print(f"Combinación {combinación}: Dado 1: {i}, Dado 2: {j}")
            combinación+=1
        j+=1
    j=1
    i+=1


#14 Calcule rango de numeros ingresados
cantidad = int(input("Ingrese cantidad de numeros: "))
i=1
menor = int(input("Ingrese numero: "))
mayor = menor
while i<cantidad:
    num = int(input("Ingrese numero: "))
    if num > mayor:
        mayor = num
    if num < menor:
        menor = num
    i+=1

print(f"El numero mayor es: {mayor} y el menor es: {menor}")
diff = mayor - menor
print(f"El rango del conjunto de números ingresados es: {diff}")

#15.1 Imprima patron triangular
cant = int(input("Ingrese cantidad de filas: "))
i = 1
while i <= cant:
    sec = "+"*i
    print(f"{sec}")
    i+=1

#15.2
cant = int(input("Ingrese cantidad de filas: "))
i = 1
while i <= cant:
    print("+"*i)
    i+=1

#16 Combinacion suma de dados igual al puntaje ingresado
dado1=1
dado2=1
puntaje = int(input("Ingrese el puntaje requerido: "))
combinacion = 0
while dado1 <= 6:
    while dado2 <= 6:
        resultado = dado1 + dado2
        if puntaje == resultado:
            print(f"La combinación {dado1} y {dado2} da como resultado {resultado}")
            combinacion += 1
        dado2 += 1
    dado2 = 1
    dado1 += 1

print(f"Existen {combinacion} posibles combinaciones que suman {puntaje}")

#Ejercicio extra 1
benefactores = int(input("Ingrese cantidad de benefactores: "))
monto = int(input("Ingrese monto total a recaudar: "))
i=1
recaudacion=0
mayor=0
while i<=benefactores:
    nombre, cantidad = input(f"Benefactor {i}, ingrese monto nombre y monto a donar separados por coma: ").split(",")
    recaudacion = recaudacion + int(cantidad)
    if int(cantidad) > mayor:
        mayor=int(cantidad)
        maximo_benefactor=nombre
    if recaudacion >= monto:
        print("Meta cumplida, se recaudó el monto deseado!")
        print(f"El benefactor {maximo_benefactor} fue quien donó mas, cuyo monto fué: {mayor}.")
        break
    if i == benefactores:
        print("Se cumplió con el numero de benefactores.")
        print(f"El benefactor {maximo_benefactor} fue quien donó mas, cuyo monto fué: {mayor}.")
    i+=1

#Ejercicio extra 2
i=3
clave = 0
while i>=0:
    num = int(input("Ingrese número de 4 digitos: "))
    first = num//1000
    menor = first
    second = (num%1000)//100
    if second < menor:
        menor = second
    third = (num%100)//10
    if third < menor:
        menor = third
    fourth = (num%100)%10
    if fourth < menor:
        menor = fourth
    if menor%2 == 0:
        clave = clave + (menor*(10**i))
        i = i - 1

print(f"La clave formada es: {clave}")
