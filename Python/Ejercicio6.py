#Franco está organizando un asado con sus amigos y necesita de tu ayuda.
# Para estimar cuánta carne necesita comprar, va a suponer que cada invitado come 0.7 Kg de carne. 
#Ayuda a Franco escribiendo un programa que permita al usuario ingresar la cantidad de invitados y 
#el precio de 1Kg. de carne, y muestre cuántos Kg de carne en total debe pedir al carnicero y 
#cuánto dinero necesita para pagar.

Kilos=0
Importecompra=0
invitados=int(input("Ingrese la cantidad de invitados "))
precio=float(input("Ingrese el precio del kilo de carne "))
Kilos=invitados*0.7
Importecompra=Kilos*precio
print(f"El importe de la compra seria de {Importecompra:.2f} con un total de {Kilos:.2f} kilogramos")