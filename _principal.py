from _datos import *
from _menu import *

def validar_puntaje():
    while True:
        try:
            puntaje = float(input("Puntaje (0-10): "))
            if 0 <= puntaje <= 10:
                return puntaje
            print("❌ Puntaje debe estar entre 0 y 10")
        except ValueError:
            print("❌ Ingresa un número válido")

def añadir():
    menu_agregar()
    separador()
    opc = pedir_opcion()
    separador()
    
    if opc == 1:  # Libro
        nombre = input("Nombre del libro: ")
        autor = input("Autor: ")
        genero = input("Género: ")
        puntaje = validar_puntaje()
        
        libro = {
            "Nombre": nombre, 
            "Autor": autor,
            "Genero": genero,
            "Puntaje": puntaje
            }
        libros.append(libro)
        guardar_libros()
        print(f"✅ Libro '{nombre}' añadido!")
        
    elif opc == 2:  # Película
        nombre = input("Nombre de la película: ")
        autor = input("Director: ")
        genero = input("Género: ")
        puntaje = validar_puntaje()
        
        pelicula = {
            "Nombre": nombre, 
            "Director": autor,
            "Genero": genero,
            "Puntaje": puntaje
            }
        peliculas.append(pelicula)
        guardar_peliculas()
        print(f"✅ Película '{nombre}' añadida!")
        
    elif opc == 3:  # Música
        nombre = input("Nombre de la música: ")
        autor = input("Artista: ")
        genero = input("Género: ")
        puntaje = validar_puntaje()
        
        musica_item = {
            "Nombre": nombre, 
            "Autor": autor, 
            "Genero": genero, 
            "Puntaje": puntaje
            }
        musicas.append(musica_item)
        guardar_musicas()
        print(f"✅ Música '{nombre}' añadida!")
    elif opc == 0:
        return

def verElem():
    menu_ver()
    separador()
    cargar_libros()
    mostrar_elementos(libros, "libros")
    cargar_peliculas()
    mostrar_elementos(peliculas, "películas")
    cargar_musicas()
    mostrar_elementos(musicas, "música")
    input("Precione Enter para ir  Menu Principal...")
    menu_principal

def busElem():
    cargar_libros()
    cargar_peliculas()
    cargar_musicas()
    
    if not (libros or peliculas or musicas):
        print("❌ No hay elementos en la colección")
        input("¿Desea seguir? Presione enter...")
        return
    
    menu_buscar()
    separador()
    opc = pedir_opcion()
    separador()
    
    buscar = input("🔍 Ingrese el elemento a buscar:_").lower().strip()
    
    if opc == 1:  # Título
        res_libros = [l for l in libros if buscar in l.get('Nombre', '').lower()]
        res_pelis = [p for p in peliculas if buscar in p.get('Nombre', '').lower()]
        res_musica = [m for m in musicas if buscar in m.get('Nombre', '').lower()]
        
    elif opc == 2:  # Autor
        res_libros = [l for l in libros if buscar in l.get('Autor', '').lower()]
        res_pelis = [p for p in peliculas if buscar in p.get('Autor', '').lower()] 
        res_musica = [m for m in musicas if buscar in m.get('Autor', '').lower()]
        
    elif opc == 3:  # Género
        res_libros = [l for l in libros if buscar in l.get('Genero', '').lower()]
        res_pelis = [p for p in peliculas if buscar in p.get('Genero', '').lower()]
        res_musica = [m for m in musicas if buscar in m.get('Genero', '').lower()]
    elif opc == 0:
        return
    
    print(f"\nLibros encontrados: {len(res_libros)}")
    mostrar_elementos(res_libros, "libros")
    print(f"Películas encontradas: {len(res_pelis)}")
    mostrar_elementos(res_pelis, "películas")
    print(f"Música encontrada: {len(res_musica)}")
    mostrar_elementos(res_musica, "música")
    input("\nPresiona Enter para continuar...")

# Editar

def edElem():
    menu_editar()
    separador()
    opc = pedir_opcion()
    separador()
    
    if opc == 1:  # Editar Título
        categoria = input("Categoría (libros/peliculas/musica): ").lower()
        buscar = input("Título actual a cambiar: ").lower().strip()
        
        if categoria == "libros":
            for libro in libros:
                if buscar in libro['Nombre'].lower():
                    nuevo_nombre = input(f"Nuevo título (actual: {libro['Nombre']}): ")
                    libro['Nombre'] = nuevo_nombre
                    guardar_libros()
                    print("✅ Título actualizado")
                    return
        print("❌ No encontrado")
        
    elif opc == 2:  # Editar Autor
        categoria = input("Categoría: ").lower()
        buscar = input("Nombre para buscar autor: ").lower().strip()
        if categoria == "libros":
            for libro in libros:
                if buscar in libro['Nombre'].lower():
                    nuevo_autor = input(f"Nuevo autor (actual: {libro['Autor']}): ")
                    libro['Autor'] = nuevo_autor
                    guardar_libros()
                    print("✅ Autor actualizado")
                    return
        print("❌ No encontrado")
        
    elif opc == 3:  # Editar Género
        categoria = input("Categoría: ").lower()
        buscar = input("Nombre para buscar género: ").lower().strip()
        if categoria == "libros":
            for libro in libros:
                if buscar in libro['Nombre'].lower():
                    nuevo_genero = input(f"Nuevo género (actual: {libro['Genero']}): ")
                    libro['Genero'] = nuevo_genero
                    guardar_libros()
                    print("✅ Género actualizado")
                    return
        print("❌ No encontrado")
        
    elif opc == 4:  # Editar Puntaje
        print("¿En que Categoría desea hacer el cambio(Música, Peliculas, Libros)?")
        categoria = input("Categoría: ").lower()

        if categoria == "libros":
            buscar = input("Nombre para buscar puntaje: ").lower().strip()
            for libro in libros:
                if buscar in libro['Nombre'].lower():
                    nuevo_puntaje = validar_puntaje()
                    libro['Puntaje'] = nuevo_puntaje
                    guardar_libros()
                    print("✅ Puntaje actualizado")
                else:
                    print("❌ Elemento no encontrado")
                
        elif categoria == "peliculas":
            buscar = input("Nombre para buscar puntaje: ").lower().strip()
            for pelicula in peliculas:
                if buscar in pelicula['Nombre'].lower():
                    nuevo_puntaje = validar_puntaje()
                    pelicula['Puntaje'] = nuevo_puntaje
                    guardar_libros()
                    print("✅ Puntaje actualizado")
                else:
                    print("❌ Elemento no encontrado")
                    
        elif categoria == "musica":
            buscar = input("Nombre para buscar puntaje: ").lower().strip()
            for musica in musica:
                if buscar in libro['Nombre'].lower():
                    nuevo_puntaje = validar_puntaje()
                    libro['Puntaje'] = nuevo_puntaje
                    guardar_libros()
                    print("✅ Puntaje actualizado:)")
                else:
                    print("❌ Elemento no encontrado")
        else:
            print("❌ Categoría inexistente:(")
    elif opc == 0:
        return

# Eliminar Elemento
def eliminarElem():
    menu_eliminar()
    separador()
    opc = pedir_opcion()
    separador()
    
    if opc == 1:  # Por título
        buscar = input("Título a eliminar: ").lower().strip()
        eliminado = False
        
        for i, libro in enumerate(libros):
            if buscar in libro['Nombre'].lower():
                print(f"🗑️ Eliminando: {libro['Nombre']}")
                libros.pop(i)
                eliminado = True
                break
                
        for i, peli in enumerate(peliculas):
            if buscar in peli['Nombre'].lower():
                print(f"🗑️ Eliminando: {peli['Nombre']}")
                peliculas.pop(i)
                eliminado = True
                break
        
        if eliminado:
            guardar_libros()
            guardar_peliculas()
            print("✅ Elemento eliminado correctamente")
        else:
            print("❌ Elemento no encontrado")
            
    elif opc == 2:  # Por ID
        categoria = input("Categoría (1=libros, 2=pelis, 3=musica): ")
        id_elem = int(input("ID a eliminar: "))
        
        if categoria == "1" and libros:
            if 1 <= id_elem <= len(libros):
                eliminado = libros.pop(id_elem - 1)
                guardar_libros()
                print(f"✅ {eliminado['Nombre']} eliminado")
            else:
                print("❌ ID inválido")
        print("❌ No hay elementos")
    elif opc == 0:
        return

# Ver por categoría
def verCategoria():
    menu_categorias()
    separador()
    opc = pedir_opcion()
    separador()
    if opc == 1:
        cargar_libros()
        mostrar_elementos(libros, "libros")
    elif opc == 2:
        cargar_peliculas()
        mostrar_elementos(peliculas, "películas")
    elif opc == 3:
        cargar_musicas()
        mostrar_elementos(musicas, "música")
    elif opc == 0:
        return

# Guardar/Cargar
def guardarCargar():
    menu_mixto()
    separador()
    opc = pedir_opcion()
    separador()
    if opc == 1:
        guardar_libros()
        guardar_peliculas()
        guardar_musicas()
        print("💾 ¡Colección guardada!")
    elif opc == 2:
        cargar_libros()
        cargar_peliculas()
        cargar_musicas()
        print("📂 ¡Colección cargada!")
    elif opc == 0:
        return
