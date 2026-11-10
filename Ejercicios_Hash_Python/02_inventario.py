inventario = {"manzanas": 20, "peras": 15, "naranjas": 30}
producto = input("Producto a buscar: ").strip().lower()
print("Existencias:", inventario.get(producto, "No encontrado"))