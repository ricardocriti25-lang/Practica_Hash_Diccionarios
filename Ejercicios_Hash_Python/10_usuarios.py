usuarios = {"ana123": "Ana", "luis456": "Luis", "maria789": "Maria"}
usuario = input("Nombre de usuario: ").strip().lower()
if usuario in usuarios:
    print("Usuario encontrado:", usuarios[usuario])
else:
    print("Usuario no encontrado")