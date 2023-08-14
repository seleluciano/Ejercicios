#Generar una lista con 10 valores enteros aleatorios entre 1 y 20 (se puede usar randint() del módulo random).
#Luego:
#1. Muestre la lista
#2. El usuario  debe ingresar un valor. El programa debe informar cuántos valores de la lista son mayores a
#dicho valor, para eso debe utilizar una función. La función debe recibir como argumentos la  lista y un entero,
#y debe retornar la cantidad de valores de la lista mayores a dicho entero.
#3. Crear una función que calcule el promedio de la lista y utilizarla.
#4. Crear una función que encuentre el valor más grande y el más pequeño de la lista y los retorne
import random
lista=[]
def cargar():
    v=0
    for i in range(10):
       v=random.randint(1, 100)
       lista.append(v)

def mostrar():
    print(lista)

def mayores(p):
    cont=0
    for elem in lista:
        if elem>p:
            cont=cont+1
    return cont

def promedio():
    suma=0
    p=0.0
    for elem in lista:
        suma=suma+elem
    p=suma/10
    return p

def maximoyminimo():
    mayor=0
    menor=102
    for elem in lista:
        if elem>mayor:
            mayor=elem
        elif menor>elem:
            menor=elem
    return(mayor,menor)

cargar()
mostrar()
x=int(input("Ingresar un valor "))
cant=mayores(x)
print(f"La cantidad de valores mayores a {x} es de {cant}")
prom=promedio()
print(f"El promedio de los elementos de la lista es de {prom}")
(max,min)=maximoyminimo()
print(f"El maximo valor de la lista es {max} y el minimo valor de la lista es {min}")



