import os 
import time

productos = []


def limpiar():
    os.system("cls")
    
def pausar():
    time.sleep(5)
    
    
def menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Eliminar producto")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar productos")
    print("6. Salir")
    print("=====================================")
    
def accion():
    try:
        while True:
            respuesta = int(input("Ingrese la accion que desea realizar"))
            if respuesta <=6 and respuesta >= 1:
                return respuesta
            else:
                print("el numero debe de estar entre las opciones definidas")
    except:
        print("tiene que ser un numero tu respuesta")
        





def _validar_str(string):
    if len(string) > 0:
        return True
    else:
        print("el campo no puede venir vacio")
        return False

def _validar_int(numero):
    if numero < 0:
        print("el numero debe de ser un entero positivo")
        return False
    else:
        return True
        
def _validar_float_(numero):
    if numero >0:
        return True
    else:
        return False
        
def agregar_producto(productos):
    while True:
        nombre = input("ingrese el nombre del producto\n").title()
        if _validar_str(nombre) == True:
            break

    
    while True:
        try:
            stock = int(input("cuantos tiene en stock?\n"))
            if _validar_int(stock) == True:
                break
        except:
            print("debes ingresar un numero")

    while True:
        try:
            precio = float(input("ingrese el precio del producto:\n"))
            if _validar_float_(precio) == True:
                break
        except:
            print("debes ingresar un numero valido")
    producto = {
        "nombre" : nombre,
        "stock" : stock,
        "precio": precio,
        "estado": False
    }
    productos.append(producto)

def _verificar_estado_(x):
    if x["estado"] == True:
        return "en stock"
    else:
        return "sin stock"
    
    
    
def buscar_producto():
    actualizar_disponibilidad()
    if len(productos) == 0:
        print("no se puede buscar ya que no hay datos registrados")
    
    else:
        busqueda = input("ingrese el nombre del producto a buscar").title()
        for p in productos:
            if p["nombre"] == busqueda:
                print(f"PRODUCTO ENCONTRADO")
                print(f"nombre: {p["nombre"]}")
                print(f"stock: {p["stock"]}")
                print(f"precio: {p["precio"]}")
                print(f"estado: {_verificar_estado_(p)}")
                break
            else:
                print("producto no encontrado")
                
def eliminar_producto():
    if len(productos) == 0:
        print("no se puede eliminar ya que no hay datos registrados")
    else:
        busqueda = input("ingrese el nombre del producto a eliminar").title()
        iterador = 0
        while iterador < len(productos):
            if productos[iterador]["nombre"] == busqueda:
                print("PRODUCTO ELIMINADO")
                productos.pop(iterador)
                break
            else:
                iterador+=1
                
                
def actualizar_disponibilidad():
    contador = 0
    while contador < len(productos):
        if productos[contador]["stock"] != 0:
            productos[contador]["estado"] = "en stock"
            contador += 1
        else:
            productos[contador]["estado"] = "sin stock"
            contador += 1
        
def mostrar_productos():
    actualizar_disponibilidad()
    print(f"LISTA DE PRODUCTOS")
    for d in productos:
        print(f"nombre: {d["nombre"]}")
        print(f"stock: {d["stock"]}")
        print(f"precio: {d["precio"]}")
        print(f"estado: {d["estado"]}")
