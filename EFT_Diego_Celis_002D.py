juegos = {
'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True,
'NovaStudio'],
'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False,
'BrightWorks'],
'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True,
'OrionGames'],
'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True,
'VelocityLab'],
'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False,
'GreenSeed'],
'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False,
'IronGate']
}
inventario = {
'G001': [9990, 7],
'G002': [19990, 0],
'G003': [42990, 3],
'G004': [14990, 5],
'G005': [17990, 9],
'G006': [39990, 2]
}
def mostrar_i():
    print(inventario)
def mostrar_j():
    print(juegos)
def stock_por_plataforma(plataf):
    cont=0
    for a in juegos.items():
        if a==plataf:
            cont+=1
    print(cont)
        

def busqueda_precio(p_min, p_max):
    juegos_en_rango=[]
    for i in inventario.items():
        if i[0]>= p_min and i[0] <=p_max:
            if i[inventario.keys()][1]==0:
                print("")
            else:
                juegos_en_rango=juegos_en_rango.append(juegos[juegos.keys()][0], juegos[juegos.keys()])
        elif juegos_en_rango==[]:
            print("No hay juegos en ese rango de precios.")
def actualizar_precio(codigo, nuevo_precio):
    while True:
        try:
            agre=int(input("Desea agregar el/un juego, 1 si, 0 no: "))
            match agre:
                case 1:
                    for a in inventario.items():
                        if codigo:
                                inventario[codigo][0]=nuevo_precio
                                print("El cambio fue exitoso")
                        else:
                            print("El codigo no existe")
                case 0:
                    print("ok")
                    break
                case _:
                    print("esa opcion no existe")
        except ValueError:
            print("error en el tipo")

def agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock):
    juegos[codigo]=[titulo, plataforma, genero, clasificacion, multiplayer, editor]
    inventario[codigo]=[precio, stock]

    
def eliminar_juego(codigo):
    for a in juegos.items():
        if codigo:
            del juegos[codigo]
            del inventario[codigo]
            print("Eliminacion exitosa")
        else:
            print("El codigo no existe")
def menu():
    while True:
        try:
            print('''========== MENÚ PRINCIPAL ==========
        1. Stock por plataforma
        2. Búsqueda de juegos por rango de precio
        3. Actualizar precio de juego
        4. Agregar juego
        5. Eliminar juego
        6. Salir
=====================================''')
            op=int(input("Ingrese la opcion: "))
            match op:
                case 1:
                    plataf=input("Ingrese la plataforma: ")
                    stock_por_plataforma(plataf)
                case 2:
                    while True:

                        try:
                            p_min=int(input("Ingrese el precio minimo: "))
                            p_max=int(input("Ingrese el precio maximo: "))
                            while p_min > p_max:
                                print("El precio minimo no puede ser mayor al maximo o al revez")
                                p_min=int(input("Ingrese el precio minimo: "))
                                p_max=int(input("Ingrese el precio maximo: "))
                            break
                        except ValueError:
                            print("error") 
                    busqueda_precio(p_min, p_max)
                case 3:
                    while True:
                        try:
                            codigo=input("Ingrese el codigo: ").upper().replace(" ", "")
                            nuevo_precio=int(input("Ingrese el nuevo precio: "))
                            while nuevo_precio <=0:
                                nuevo_precio=int(input("El juego no puede tener un precio menor o igual a 0"))
                            break
                        except ValueError:
                            print("error en el tipo")
                    actualizar_precio(codigo, nuevo_precio)
                    
                case 4:
                    while True:
                        try:
                            codigo=input("ingrese el codigo: ").upper().replace(" ","")
                            while codigo in juegos.items() or codigo== "":
                                codigo=input("ingrese un codigo que no exista o que no este en blanco: ").upper().replace(" ","")
                            titulo=input("Ingrese el titulo: ")
                            while titulo=="":
                                titulo=input("Ingrese un titulo válido: ")
                            plataforma=input("Ingrese la plataforma: ")
                            while plataforma=="":
                                plataforma=input("Ingrese la plataforma: ")
                            genero=input("Ingrese el genero: ")
                            while genero=="":
                                genero=input("Ingrese el genero: ")
                            clasificacion=input("Ingrese la clasificación (E, T o M): ").upper()
                            while clasificacion not in "ETM":
                                clasificacion=input("Ingrese la clasificación (E, T o M): ").upper()
                            multiplayer=input("Tiene multiplayer? (si o no): ").lower()
                            while multiplayer not in "sino":
                                multiplayer=input("Tiene multiplayer? (si o no): ").lower()
                            if multiplayer=="si":
                                multiplayer= True
                            else:
                                multiplayer= False
                            
                            editor=input("Ingrese el editor: ")
                            while editor=="":
                                editor=input("Ingrese el editor: ")
                            precio=int(input("Ingrese el precio: "))
                            while precio<=0:
                                precio=int(input("El precio no puede ser igual o menor a 0, ingrese el precio: "))
                            stock=int(input("Ingrese el stock: "))
                            while stock < 0:
                                stock=int(input("El stock no puede ser un numero negativo, ingrese stock: "))
                            break
                        except ValueError:
                            print("error en el tipo")
                    agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock)
                    
                case 5:
                    codigo=input("Ingrese el codigo del juego que quiere eliminar: ").upper().replace(" ", "")
                    eliminar_juego(codigo)
                case 6:
                    print("Saliendo")
                    break
                case _:
                    print("esa opción no existe")

        except ValueError:
            print("Error en el tipo")

menu()



