# Ejercicio 09: Actualizacion de existencias mediante clave
# Diccionario: estructura clave-valor para busqueda rapida.

productos = {"laptop": 5, "mouse": 10, "teclado": 8}
print("Inventario inicial:", productos)
producto = input("Producto a actualizar: ").strip().lower()
if producto in productos:
    cantidad = int(input("Nueva cantidad: "))
    if cantidad >= 0:
        productos[producto] = cantidad
        print("Inventario actualizado:", productos)
    else:
        print("La cantidad no puede ser negativa")
else:
    print("Producto no encontrado")
