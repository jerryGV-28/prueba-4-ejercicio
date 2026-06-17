import os 
import time

productos = []
#producto = {
#    "nombre" = "",
#    "stock" = "" ,
#    "precio" = "" ,
#    "disponible" = ""
#}

def limpiar():
    os.system("cls")
    
def pausar():
    time.sleep(2)

def _validar_str(string):
    if len(string) > 0:
        return True
    else:
        print("el campo no puede venir vacio")
        return False

def _validar_int(numero):
    if numero <= 0:
        print("el numero debe de ser un entero positivo")
        return False
    else:
        return True
        
    
def agregar_producto(productos):
    while True:
        nombre = input("ingrese el nombre del producto\n").title().split()
        if _validar_str(nombre) == True:
            break

    
    while True:
        try:
            stock = int(input("cuantos tiene en stock?\n"))
            if _validar_int(stock) == True:
                break
        except:
            print("debes ingresar un numero")
