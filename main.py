from functions import *
limpiar()

while True:
    limpiar()
    menu()
    eleccion = accion()
    if eleccion == 1:
        limpiar()
        agregar_producto(productos)
        pausar()
    elif eleccion == 2:
        limpiar()
        buscar_producto()
        pausar()
    elif eleccion == 3:
        limpiar()
        eliminar_producto()
        pausar()
    elif eleccion == 4:
        limpiar()
        actualizar_disponibilidad()
        pausar()
    elif eleccion == 5:
        limpiar()
        mostrar_productos()
        pausar()
    elif eleccion == 6:
        print("muchas gracias")
        break