precios = {"leche": 28, "pan": 15, "huevo": 45}
producto = input("Producto a consultar: ").strip().lower()
precio = precios.get(producto)
print(f"Precio: ${precio}" if precio is not None else "Producto no encontrado")