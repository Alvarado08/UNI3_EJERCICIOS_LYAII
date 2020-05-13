#!/usr/bin/python3
#*****************************
#SECCION DE EJERCICIOS LOCALES
#*****************************
#EJERCICIO 1 LOCAL
#CODIGO ORIGINAL
a = 3
b = 5
c = 2
suma = a + b
resta = a - b
print(suma) 
#CODIGO OPTIMIZADO
#CODIGO Y VARIABLES INECESARIAS FUERON ELIMINADAS
a = 3
b = 5
print(a+b)
#EJERCICIO 2 LOCAL
#CODIGO ORIGINAL
x = 4
y = 1
z = 3
op1 = x-1
op2 = y * z
final = op1 + op2
print(final)
#CODIGO OPTIMIZADO
#DEFINICION DE LOS VALORES DE LAS VARIABLES Y UNION DE VARIABLE FINAL
x,y,z = 4,1,3
final = (x-1) + (y * z)
print(final)
#EJERCICIO 3 LOCAL
#CODIGO ORIGINAL
x = 1
y = 2
z = x + x 
z2 = x + x
a = y + y 
b = x + y 
print(b)
#CODIGO OPTIMIZADO
#ELIMINACION DE LOS DATOS REPETIDOS E INICESARIOS 
x,y = 1,2
b = x + y
print (b) 
#****************************
#SECCION DE EJERCICIOS CICLOS
#****************************
#EJERCICIO 4 CICLO
#CODIGO ORIGINAL
for j in [0,1,2]:
    print("Hola")
#CODIGO OPTIMIZADO
#CREAMOS VARIABLE PARA ARREGLO Y POSTERIORMENTE SE UTILZA EN LA CONDICION FOR. DE IGUAL MANERA UN END PARA LA IMPRESION EN UNA SOLA LINEA
g = [0,1,2]
for j in g:
    print("Hola ", end='')
print("\n")
#EJERCICIO 5 CICLO
#CODIGO ORIGINAL
x2 = 0
y2 = "While"
while x2 < 5:
    x2 += 1
    print(y2)
print("\n")
#CODIGO OPTIMIZADO
#ELIMINACION DE VARIABLE ADICIONAL CON EL VALOR PARA IMPRIMIR
x1 = 0
while x1 < 5:
    x1 += 1
    print("While")
#EJERCICIO 6 CICLO
#CODIGO ORIGINAL
a1 = [1,2,3]
for b1 in a1:
    c1 = b1 + 1
    res = "Suma de 1 + " + str(b1) + " = " + str(c1)
    print(res)
#CODIGO OPTIMIZADO
#ELIMINACION DE CONCATENACION Y EXCESO DE VARIABLES
a1 = [1,2,3]
for b1 in a1:
    print(f"Suma de 1 + {b1} = {b1+1}")
#*****************************
#SECCION DE EJERCICIOS MIRILLA
#*****************************
#EJERCICIO 7 MIRILLA
#CODIGO ORIGINAL
z1 = 0
while z1 < 4:
    z1 += 1
    if z1 == 3:
        print(z1)
    else:
        pass
#CODIGO OPTIMIZADO
#TERMINAMOS DE MANERA DEFINIDA CON UN BREAK EVITANDO ELEMENTOS INECESARIOS AL QUITAR PASS, INTERRUMPIENDO EL FLUJO
z1 = 0
while z1 < 4:
    z1 += 1
    if z1 == 3:
        print(z1)
        break
#EJERCICIO 8 MIRILLA
#CODIGO ORIGINAL
for z in "itsva":
    v = "v"
    if z == v:
        pass
    else:
        print(z)
#CODIGO OPTIMIZADO
#ELIMINACION DE VARIABLE PARA LIBERAR ESPACIO Y EL USO DEL BREAK PARA TERMINAR DE MANERA DEFINIDA, INTERRUMPIENDO EL FLUJO
for z in "itsva":
    if z == "v":
        break
    print(z)
#EJERCICIO 9 MIRILLA
#CODIGO ORIGINAL
i = 0
j = "Linea 1"
while i < 3:
    i += 1
    print(j)
#CODIGO OPTIMIZADO
#ELIMINACION DE VARIABLE INECESARIA
i = 0
while i < 3:
    i += 1
    print("Hola")
    break
#******************************
#SECCION DE EJERCICIOS GLOBALES
#******************************
#EJERCICIO 10 GLOBAL
#CODIGO ORIGINAL
contenido = "Hola mundo, es hora de programar!"
file = "archivo.txt"
archivo = open(file, 'w')
archivo.write(contenido) 
archivo.close()

archivo2 = open(file, "r")
for linea in archivo2.readlines():
    print(linea)
archivo2.close() 
#CODIGO OPTIMIZADO
#SE OPTIMIZO SECCION DE LEER ARCHIVO INTERCAMBIANDO EL CICLO 'FOR' POR UNA BUSQUEDA DE POSICION, POSTERIORMENTE IMPRIMIENDOLO
archivo3 = open(file,"r")
archivo3.seek(0)
print(archivo3.read())
archivo3.close()  