#Un club deportivo tiene 4 categorías de asociados según la edad:
#infantiles (desde 13 a 15 años)
#cadetes (a partir de los 15 y hasta 17)
#juveniles (desde los 17 hasta los 19)
#mayores (de 19 años en adelante)
#Escriba un programa que permita al usuario ingresar el nombre y la edad de un socio 
# y muestre su el nombre de la categoría en la que le corresponde estar

edad=int(input("Ingrese la edad del socio "))
nombre=input("Ingrese el nombre del socio ")

if edad>=13 and edad<=15:
    print(f"{nombre} de {edad} años pertenece a la categoria Infantil")
elif edad>15 and edad<=17:
    print(f"{nombre} de {edad} años pertenece a la categoria Cadete")
elif edad>17 and edad<=19:
    print(f"{nombre} de {edad} años pertenece a la categoria Juvenil")
else:
    print(f"{nombre} de {edad} años pertenece a la categoria Mayor")
   