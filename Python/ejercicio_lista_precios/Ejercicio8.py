import db_productos
productos = []

def mostrar():
    for elem in productos:
        print(f'Producto: {elem["id"]}')
        print(f'Nombre: {elem["nombre"]}')
        print(f'Precio: {elem["precio"]}')

def calcular_precio_actualizado(p,aum):
    p=p+(p*aum)
    return p

def actualizar_precios(aument):
    viejoprecio=0.0
    precioactualizado=0.0
    for elem in productos:
        viejoprecio=elem["precio"]
        precioactualizado=calcular_precio_actualizado(viejoprecio,aument)
        elem["precio"]=precioactualizado

def lista_precios_actualizados():
    print("*****PRECIOS ACTUALIZADOS*****")
    for elem in productos:
        print(f'Producto: {elem["id"]}')
        print(f'Nombre: {elem["nombre"]}')
        print(f'Precio: {elem["precio"]}')

productos=db_productos.cargar_productos()
mostrar()
aumento=float(input("Ingrese el aumento "))
actualizar_precios(aumento)
lista_precios_actualizados()

