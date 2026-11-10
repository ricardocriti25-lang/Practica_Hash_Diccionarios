estudiantes = {101: "Ana", 102: "Luis", 103: "Maria"}
matricula = int(input("Matricula a buscar: "))
print("Resultado:", estudiantes.get(matricula, "No encontrado"))