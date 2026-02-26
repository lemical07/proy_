from _menu import menu_principal, separador, pedir_opcion
from _principal import añadir, verElem, busElem, edElem, eliminarElem, verCategoria, guardarCargar, verEstadisticas
from _datos import cargar_libros, cargar_peliculas, cargar_musicas, guardar_libros, guardar_peliculas, guardar_musicas
# Carga inicial
cargar_libros()
cargar_peliculas()
cargar_musicas()

while True:
    separador()
    menu_principal()
    separador()
    opcion = pedir_opcion()
    separador()
    
    if opcion == 1:
        añadir()
    elif opcion == 2:
        verElem()
    elif opcion == 3:
        busElem()
    elif opcion == 4:
        edElem()
    elif opcion == 5:
        eliminarElem()
    elif opcion == 6:
        verCategoria()
    elif opcion == 7:
        guardarCargar()
    elif opcion==8:
        verEstadisticas()
    elif opcion == 0:
        print("¡Salida exitosa!")
        guardar_libros()
        guardar_peliculas()
        guardar_musicas()
        break
    else:
        print("❌ Opción incorrecta")
