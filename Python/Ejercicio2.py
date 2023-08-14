#Durante los 5 días de una semana se tomaron mediciones de temperatura en la ciudad.
# Se desea conocer cuál fue la temperatura promedio de la semana. 
#Escriba un programa que permita calcularla a partir de 5 valores de temperatura que ingresará el usuario
suma=0
for i in range(5):
    temperatura=float(input("Ingrese la temperatura del dia ",i+1))
    suma=temperatura+suma
promedio= suma/5
print("El promedio de las temperaturas de la semana es:",promedio)
