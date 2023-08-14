#Escriba un programa que permita a una persona conocer a cuántos Pesos Argentinos 
#equivalen hoy los Bitcoins (BTC) que encontró guardados en un disco rígido viejo. 
#El usuario del programa debe ingresar una cantidad en Bitcoins.
Pesos=0
Bitcoins=float(input("Ingrese la cantidad de Bitcoins que quiere convertir a pesos argentinos"))
Pesos = 8265686.62*Bitcoins
print(f"Con {Bitcoins} obtendra $ {Pesos}")