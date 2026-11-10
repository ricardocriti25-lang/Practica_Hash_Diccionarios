libros = {1: "Matematicas", 2: "Programacion", 3: "Historia"}
codigo = int(input("Codigo del libro: "))
print("Libro:", libros.get(codigo, "No encontrado"))