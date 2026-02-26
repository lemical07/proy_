from json import load, dumps
import os

libros = []
peliculas = []
musicas = []
estadistica=[]

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

#  IDs ÚNICOS
def proximo_id(coleccion):
    """Devuelve el siguiente ID único"""
    if not coleccion:
        return 1
    return max(item.get('ID', 0) for item in coleccion) + 1

def agregar_libro(nombre, autor, genero, puntaje):
    """Agrega libro con ID único"""
    global libros
    nuevo_id = proximo_id(libros)
    libro = {
        "ID": nuevo_id,
        "Nombre": nombre,
        "Autor": autor,
        "Genero": genero,
        "Puntaje": puntaje
    }
    libros.append(libro)
    escribir_json("libros.json", libros)
    return nuevo_id

def agregar_pelicula(nombre, autor, genero, puntaje):
    """Agrega película con ID único"""
    global peliculas
    nuevo_id = proximo_id(peliculas)
    pelicula = {
        "ID": nuevo_id,
        "Nombre": nombre,
        "Autor": autor,
        "Genero": genero,
        "Puntaje": puntaje
    }
    peliculas.append(pelicula)
    escribir_json("peliculas.json", peliculas)
    return nuevo_id

def agregar_musica(nombre, autor, genero, puntaje):
    """Agrega música con ID único"""
    global musicas
    nuevo_id = proximo_id(musicas)
    musica_item = {
        "ID": nuevo_id,
        "Nombre": nombre,
        "Autor": autor,
        "Genero": genero,
        "Puntaje": puntaje
    }
    musicas.append(musica_item)
    escribir_json("musica.json", musicas)
    return nuevo_id

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
    print("-" * 60)
    for elem in elementos: 
        print(f"ID: {elem['ID']} | {elem['Nombre']} - {elem['Autor']}")
        print(f"  Género: {elem['Genero']} | Puntaje: {elem['Puntaje']}")
        print("-" * 60)

def guardar_estadistica():
    escribir_json("estadistica.json",estadistica)

def cargar_estadisticas():
    global estadistica
    estadistica.clear()
    estadistica.extend(leer_json("estadistica.json"))

