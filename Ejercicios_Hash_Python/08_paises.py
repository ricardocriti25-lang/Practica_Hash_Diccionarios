capitales = {"mexico": "Ciudad de Mexico", "francia": "Paris", "japon": "Tokio"}
pais = input("Pais: ").strip().lower()
print("Capital:", capitales.get(pais, "No encontrado"))