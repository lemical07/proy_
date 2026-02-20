from json import load, dumps
import os

libros = []
peliculas = []
musicas = []

def leer_json(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        return []
    try:
        with open(nombre_archivo, "r", encoding='utf-8') as file:
            return load(file)
    except:
        return []

def escribir_json(nombre_archivo, contenido):
    try:
        with open(nombre_archivo, "w", encoding='utf-8') as file:
            file.write(dumps(contenido, indent=4, ensure_ascii=False))
    except Exception as e:
        print(f"❌ Error guardando {nombre_archivo}: {e}")

def guardar_libros():
    escribir_json("libros.json", libros)

def cargar_libros():
    global libros
    libros.clear()
    libros.extend(leer_json("libros.json"))

def guardar_peliculas():
    escribir_json("peliculas.json", peliculas)

def cargar_peliculas():
    global peliculas
    peliculas.clear()
    peliculas.extend(leer_json("peliculas.json"))

def guardar_musicas():
    escribir_json("musica.json", musicas)

def cargar_musicas():
    global musicas
    musicas.clear()
    musicas.extend(leer_json("musica.json"))

def mostrar_elementos(elementos, tipo):
    if not elementos:
        print(f"No hay {tipo} en la colección.")
        return
    
    print(f"\n {len(elementos)} {tipo}(s) encontrados:")
    print("-" * 50)
    for i, elem in enumerate(elementos, 1):
        print(f"{i}. ID: {i} | {elem['Nombre']} - {elem['Autor']}")
        print(f"   Género: {elem['Genero']} | Puntaje: {elem['Puntaje']}")
    print("-" * 50)