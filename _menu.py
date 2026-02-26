def menu_principal():
    menu1 = """
    ================================
          Administrar Colección
    ================================
    ¿Qué desea hacer?
    1. Añadir un Nuevo Elemento
    2. Ver Todos los Elementos  
    3. Buscar un Elemento
    4. Editar un Elemento
    5. Eliminar un Elemento
    6. Ver Elementos por Categoría
    7. Guardar y Cargar Colección
    8. Estadísticas
    0. Salir
    """
    print(menu1)

def menu_agregar():
    menu2 = """
    ================================
         Añadir un Nuevo Elemento
    ================================
    ¿Qué tipo de elemento deseas añadir?
    1. Libro
    2. Película
    3. Música
    0. Regresar al Menú Principal
    """
    print(menu2)

def menu_ver():
    menu3 = """
    ================================
          Ver todos los Elementos
    ================================
    ¿Qué categoría deseas ver?
    1. Ver Todos los Libros
    2. Ver Todas las Películas
    3. Ver Toda la Música
    0. Regresar al Menú Principal
    """
    print(menu3)

def menu_buscar():
    menu4 = """
    ================================
           Buscar un Elemento
    ================================
    ¿Cómo deseas buscar?
    1. Buscar por Título
    2. Buscar por Autor/Director/Artista
    3. Buscar por Género
    0. Regresar al Menú Principal
    """
    print(menu4)

def menu_editar():
    menu5 = """
    ================================
           Editar un Elemento
    ================================
    ¿Qué deseas editar?
    1. Editar Título
    2. Editar Autor/Director/Artista
    3. Editar Género
    4. Editar Valoración
    0. Regresar al Menú Principal
    """
    print(menu5)

def menu_eliminar():
    menu6 = """
    ================================
         Eliminar un Elemento
    ================================
    ¿Cómo deseas eliminar?
    1. Eliminar por Título
    2. Eliminar por Identificador Único
    0. Regresar al Menú Principal
    """
    print(menu6)

def menu_categorias():
    menu7 = """
    ================================
        Ver Elementos por Categoría
    ================================
    ¿Qué categoría deseas ver?
    1. Ver Libros
    2. Ver Películas
    3. Ver Música
    0. Regresar al Menú Principal
    """
    print(menu7)

def menu_mixto():
    menu8 = """
    ================================
        Guardar y Cargar Colección
    ================================
    ¿Qué deseas hacer?
    1. Guardar la Colección Actual
    2. Cargar una Colección Guardada
    0. Regresar al Menú Principal
    """
    print(menu8)

def menu_est():
    menu9 = """
    ================================
              Estadísticas
    ================================
    1.Total de elementos en la colección
    2.Total de elementos por categoría
    3.Promedio general de la colección
    0. Regresar al Menú Principal

"""
    print(menu9)

def separador():
    print("=" * 50)

def pedir_opcion():
    while True:
        try:
            opc = int(input("Ingrese la opción: "))
            return opc
        except ValueError:
            print("❌ Solo números válidos")