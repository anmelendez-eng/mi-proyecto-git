# Definimos nuestra "base de datos" temporal en la memoria RAM usando un diccionario
agenda_contactos = {
    "Andres": "555-1234",
    "Mama": "555-5678"
}

def mostrar_contactos(agenda):
    print("\n--- LISTA DE CONTACTOS ---")
    for nombre, telefono in agenda.items():
        print(f"Nombre: {nombre} | Teléfono: {telefono}")

# Probamos nuestra función
mostrar_contactos(agenda_contactos)