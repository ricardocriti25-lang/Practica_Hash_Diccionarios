empleados = {201: "Gerente", 202: "Cajero", 203: "Vendedor"}
identificador = int(input("ID del empleado: "))
print("Puesto:", empleados.get(identificador, "No encontrado"))