"""1. Ingresar valor 1
2. Ingresar valor 2
3. Mostrar suma
4. Mostrar resta
5. Mostrar multiplicación
6. Mostrar división
7. Salir"""

def suma(x,y):
    sum=0
    sum=x+y
    print(f"La suma es: {sum}")

def resta(x,y):
    rest=0
    rest=x-y
    print(f"La resta es: {rest}")

def multiplicacion(x,y):
    mult=0
    mult=x*y
    print(f"La multiplicacion es: {mult}")

def division(x,y):
    div=0
    div=x/y
    print(f"La division es: {div}")


print("*****Elija la opcion*****")
print("1 Ingresar valores \n 2 Sumar  \n 3 Restar  \n 4 Multiplicar \n 5 Division \n 6 Salir \n")
n=int(input("Elija una opcion"))
while n!=6:
    if n==1:
        X= float(input("Ingrese un valor "))
        Y= float(input("Ingrese otro valor "))
    elif n==2:
        suma(X,Y)
    elif n==3:
        resta(X,Y)
    elif n==4:
        multiplicacion(X,Y)
    elif n==5:
        division(X,Y)
    print("*****Elija la opcion*****")
    print("1 Ingresar valores \n 2 Sumar  \n 3 Restar  \n 4 Multiplicar \n 5 Division \n 6 Salir \n")
    n=int(input("Elija una opcion"))
print("*****FIN, GRACIAS*****")