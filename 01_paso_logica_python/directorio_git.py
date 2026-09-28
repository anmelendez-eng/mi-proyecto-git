#python directorio_git.py

import json #traduce diccionarios a formato JSOn y viciversa
import os #Operating System (Sistema Operativo): 
#Pregunta a windows si el archivo ya existe en el disco duro antes de intentar leerlo

# Definimos el nombre del archivo donde vivirá nuestra persistencia
ARCHIVO_DATOS = "agenda.json" #Declaracion de constante

def cargar_agenda():
    if os.path.exists(ARCHIVO_DATOS):  # Si el archivo JSON ya existe en el disco duro, lo leemos
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
            #UTF-8 (El estándar mundial moderno): Significa Unicode Transformation Format - 8-bit. 
            # Formato universal de codificacion de texto que traduce y guarda los textos como (~, acentos etc)
            #"r" esta r permite abrir este archivo únicamente para0 "leer" lo que hay adentro. .
            #No para borrarlo, modificarlo ni escribirle nada nuevo en este momento."
            #"a" "append" si solo quieres agregar datos al final sin borrar lo anterior,             
            return json.load(archivo) # Traduce el JSON del disco a un diccionario de Python
    else:
        # Si no existe (es la primera vez que corre), regresamos una agenda por defecto
        return {"Andres": "555-1234", "Mama": "555-5678"}

def guardar_agenda(agenda):
    # Tomamos el diccionario de la RAM y lo escribimos de forma permanente en el disco duro
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
        #"w" "write" queremos guardar o sobrescribir datos ene ste archivo
        json.dump(agenda, archivo, indent=4, ensure_ascii=False)
        # 2. json.dump toma tu diccionario de la RAM y lo estampa en texto plano dentro del archivo JSON
        # indent=4 le da un formato estético (con sangrías) para que los humanos podamos leerlo fácil.
    print("¡Datos guardados con éxito en el disco duro!")

# --- FLUJO PRINCIPAL DE PRUEBA ---
# 1. Al arrancar, cargamos lo que haya en el disco (o los valores por defecto si es nuevo)
agenda_contactos = cargar_agenda()

print("Agenda actual en memoria:", agenda_contactos)

# 2. Imaginemos que agregamos un nuevo contacto mediante interacción 
#  asi modificamos la agenda agregando un nuevo contacto en la RAM
nuevo_nombre = "Carlos"
nuevo_telefono = "555-9999"
agenda_contactos[nuevo_nombre] = nuevo_telefono

# 3. Guardamos los cambios permanentemente en el disco duro antes de cerrar el programa
guardar_agenda(agenda_contactos)

# --- MINI EJERCICIO: BUSCAR UN CONTACTO ---
print("\n--- BUSCANDO UN CONTACTO ---")

# Definimos el nombre que queremos buscar (puedes cambiarlo para probar)
nombre_a_buscar = "Juana"

# 1. Verificamos si la llave (nombre) existe dentro de las llaves del diccionario
if nombre_a_buscar in agenda_contactos:
    # Si existe, extraemos su valor asociado (el teléfono)
    telefono_encontrado = agenda_contactos[nombre_a_buscar]
    print(f"¡Contacto encontrado! El teléfono de {nombre_a_buscar} es: {telefono_encontrado}")
else:
    # Si no existe, informamos educadamente al usuario
    print(f"Lo sentimos, el contacto '{nombre_a_buscar}' no existe en la agenda.")