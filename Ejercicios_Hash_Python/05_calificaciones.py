calificaciones = {"ana": 9, "pedro": 8, "sofia": 10}
alumno = input("Alumno a buscar: ").strip().lower()
print("Calificacion:", calificaciones.get(alumno, "No encontrado"))