def validar_codigo(codigo):
    return len(codigo.strip()>0)

def validar_titulo(titulo):
    return len(titulo.strip())>0

def validar_plataforma(plataforma):
    return len(plataforma.strip())>0

def validar_genero(genero):
    return len(genero.strip())>0

def validar_clasificacion(clasificacion):
    clasificacion

def validar_multiplayer(multiplayer):
    multiplayer

def validar_editor(editor):
    return len(editor.strip())>0

def validar_precio(precio):
    return int and precio>0

def validar_stock(stock):
    return int and stock>=0

juegos = {'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True, 'NovaStudio'],
    'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False, 'BrightWorks'],
    'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True, 'OrionGames'],
    'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True, 'VelocityLab'],
    'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False, 'GreenSeed'],
    'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False, 'IronGate'],
}

inventario = {
    'G001': [9990, 7],
    'G002': [19990, 0],
    'G003': [42990, 3],
    'G004': [14990, 5],
    'G005': [17990, 9],
    'G006': [39990, 2],
}


def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Stock por plataforma")
    print("2. Búsqueda de juegos por rango de precio")
    print("3. Actualizar precio de juego")
    print("4. Agregar juego")
    print("5. Eliminar juego")
    print("6. Salir")
    print("=====================================")

def leer_opcion():
    while True:
        try:
            opcion=int(input("Ingrese opción: "))
            if 1< opcion <=6:
                return opcion
            print("Error: Debe de ingresar un numero entero")
        except ValueError:
            print("Error: Debe de ingresar un numero entero")

def stock_plataforma(plataforma):
    for i in range(len(plataforma)):
        if plataforma["titulo"]=="titulo":
            return i

def busqueda_precio(p_min, p_max):
    for i in range(len(inventario)):
        if p_min [i]== 9990.7:
            return 1
        else:
            p_max [i]>= 42990.0 # type: ignore
            return -1
def buscar_codigo(codigo):
    for i in range(len(inventario)):
        if codigo[i]["titulo"]=="titulo":
            return True
        else:
            return False

def actualizar_precio(codigo, nuevo_precio):
    codigo=input("Ingrese código del juego: ")
    while True:
        try:
            if codigo == [inventario]:
                return
            else:
                print("¿Desea actualizar otro precio (s/n)? ")
                if True == "s":
                    return
                else:
                    "n"== False
                    break
        except ValueError:
            print("Error: El codigo no puede tener espacios blancos.")

def agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock):
    titulo=input("Ingrese código del juego: ")
    if not validar_titulo(titulo):
        print("Error: El nombre no puede estar vacio")
        return
    titulo=titulo.strip()
    nuevo_juego= {
        "titulo":titulo,
        "codigo":codigo,
        "plataforma":plataforma,
        "genero":genero,
        "clasificacion":clasificacion,
        "multiplayer":multiplayer,
        "editor":editor,
        "precio":precio,
        "stock":stock
    }
    titulo.append(nuevo_juego)

def buscar_codigo(codigo):
    buscar_codigo(codigo)

def eliminar_juego(codigo):
    titulo=input("Ingrese el nombre del juego a eliminar: ")
    indice=buscar_codigo(codigo)
    if indice!=1:
        del juegos[indice]
        print("Juego eliminado")
    else:
        print("El código no existe")

mostrar_menu()
while True:
    opcion=leer_opcion()
    if opcion == 1:
        stock_plataforma()
    elif opcion== 2:
        busqueda_precio()
    elif opcion==3:
        agregar_juego()
    elif opcion==4:
        agregar_juego()
    elif opcion==5:
        eliminar_juego()
    else:
        opcion==6
        break
