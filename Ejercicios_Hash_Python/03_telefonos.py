telefonos = {"ana": "4411234567", "luis": "4419876543", "carlos": "4415551234"}
nombre = input("Nombre a buscar: ").strip().lower()
print("Telefono:", telefonos.get(nombre, "No encontrado"))