# pokemons={
#     1:{"nombre":"Ekans", "nivel": 19 },
#     2:{"nombre":"Gastly", "nivel": 18 },
#     3:{"nombre":"Golduck", "nivel": 52 },
#     4:{"nombre":"Eevee", "nivel": 12 }
# } 
# print(list(pokemons.keys())[-1]+1)
# print(pokemons.keys())
# print(pokemons.values())
# print(pokemons.items())
# # # list()
# # for num, pkm in pokemons.items():
# #     print(num, pkm)
# def mostrar():
#     for p, z in pokemons.items():
#         print(f"{p}.- {z} ")
#     print("-"*30)
# def eliminar():
#     mostrar()
#     # borrar_pokemon=input("Cual es el pokemon que va a liberar ?: ")
#     # pokemons.remove(borrar_pokemon)
#     borrar_pokemon=int(input("Cual es el pokemon que va a liberar ?: "))
#     del pokemons[borrar_pokemon]
# def actualizar():
#     mostrar()
#     actualizar=int(input("que pokemon desea actualizar: "))
#     nombre=input("Ingrese el nombre del pokémon: ")
#     nivel=input("Ingrese el nivel del pokémon: ")
#     pokemons[actualizar]={"nombre":nombre, "nivel": nivel }
#     print("actualizado con exito")
# def agregar():
#     pkm=input("Ingrese el nombre del pokemon: ")
#     nvl=input("Ingrese el nivel del pokemon: ")
#     pokemons[list(pokemons.keys())[-1]+1]={"nombre":pkm, "nivel": nvl }
# def menuPokemon():
#     while True:
#         try:
#             print("1.- Agregar Pokemon")
#             print("2.- Eliminar Pokemon")
#             print("3.- Actualizar Pokemon")
#             print("4.- Mostrar Pokemons")
#             print("5.- Salir")
#             op=int(input("Seleccione una opcion: "))
#             match op:
#                 case 1:
#                     agregar()
#                 case 2:
#                     eliminar()
#                 case 3:
#                     actualizar()
#                 case 4:
#                     mostrar()
#                 case 5:
#                     print("Saliendo")
#                     break
#                 case _:
#                     print("Opcion Invalida")

#         except ValueError as e:
#             print("Solo numeros enteros. Error",e)
#########################################################
# menuPokemon()

# print(list(pokemons.keys())[-1]+1)

# productos={
#     1:{"nombre":"Uva", "precio": 2000 },
#     2:{"nombre":"Palta", "precio": 4000 },
#     3:{"nombre":"Pera", "precio": 1500 }
# } 

# # usar como ejemplo el menu CRUD de pokemon
# # para hacerlo con  productos y relizar el
# # menu a continuacion


# '''
#             print("1.- Agregar Producto")
#             print("2.- Eliminar Producto")
#             print("3.- Actualizar Producto")
#             print("4.- Mostrar Productos")
#             print("5.- Comprar Productos")
#             print("6.- Crear Boleta (calcula IVA) y Salir")
#             op=int(input("Seleccione una opcion: "))'''

# ### SOLUCION

# # menuProductos()

# # print(list(productos.keys())[-1]+1)
# # productos={
# #     1:{"nombre":"Uva", "precio": 2000 },
# #     2:{"nombre":"Palta", "precio": 4000 },
# #     3:{"nombre":"Pera", "precio": 1500 }
# # } 
# carrito=[]
# def mostrar():
#     for num, prod in productos.items():
#         print(f"{num}.- {prod['nombre']}  ${prod['precio']}")
#     print("-"*30)
# def eliminar():
#     mostrar()
#     # borrar_pokemon=input("Cual es el pokemon que va a liberar ?: ")
#     # pokemons.remove(borrar_pokemon)
#     try:
#         borrar_producto=int(input("Cual es el producto que va a eliminar ?: "))
#         if borrar_producto in productos:
#             del productos[borrar_producto]
#         else:
#             print("Producto no existe")
#     except ValueError:
#         print("Debe ingresar un número válido")
# def actualizar():
#     mostrar()
#     try:
#         key=int(input("que producto desea actualizar: "))
#         if key in productos:
#             nombre=input("Ingrese el nombre del producto: ")
#             precio=int(input("Ingrese el precio del producto: "))
#             productos[key]={"nombre":nombre, "precio": precio }
#             print("actualizado con exito")
#         else:
#             print("Producto no existe")
#     except ValueError:
#         print("ID o precio inválido")
# def agregar():
#     pkm=input("Ingrese el nombre del producto: ")
#     try:
#         nvl=int(input("Ingrese el precio del producto: "))
#     except ValueError:
#         print("Precio inválido, usando 0")
#         nvl=0
#     productos[list(productos.keys())[-1]+1]={"nombre":pkm, "precio": nvl }
# def comprar():
#     while True:
#         mostrar()
#         try:
#             comprar=int(input("Cual producto desea comprar ? ( para salir, ponga 0): "))
#             if comprar==0:
#                 break
#             if comprar in productos:
#                 print(f"Usted ha comprado {productos[comprar]['nombre']} por un valor de {productos[comprar]['precio']}")
#                 carrito.append(productos[comprar])
#             else:
#                 print("Producto no existe")
#         except ValueError:
#             print("Debe ingresar un número válido")
# def boleta():
#     total=0
#     print("-"*30, "0", "-"*30)
#     print("Bienvenido a minimarquet Lost Woods")
#     print("-"*30, "0", "-"*30)
#     for p in carrito:
#         total+=int(p["precio"])
#         print(p["nombre"],"---$", p["precio"])
#     iva=total*0.19
#     print("-"*30, "0", "-"*30)
#     print(f"El total de su compra es {total} y el IVA es {iva}")
#     print(f"El total a pagar es  {total+iva} ")
#     print("Gracias por comprar en minimarquet Lost Woods")
#     print("-"*30, "0", "-"*30)
# def menuProductos():
#     while True:
#         try:
#             print("1.- Agregar Producto")
#             print("2.- Eliminar Producto")
#             print("3.- Actualizar Producto")
#             print("4.- Mostrar Productos")
#             print("5.- Comprar Productos")
#             print("6.- Crear Boleta (calcula IVA) y Salir")
#             op=int(input("Seleccione una opcion: "))
#             match op:
#                 case 1:
#                     agregar()
#                 case 2:
#                     eliminar()
#                 case 3:
#                     actualizar()
#                 case 4:
#                     mostrar()
#                 case 5:
#                     comprar()
#                 case 6:
#                     boleta()
#                     break
#                 case _:
#                     print("Opcion Invalida")

#         except ValueError as e:
#             print("Solo numeros enteros. Error",e)


# menuProductos()

##reto 1
# Cambiar el menu 5 para que sea recursivo
# Voy a seguir comprando hasta que el usuario 
# ponga  condicion para salir.
##Reto 2
# Hacer que la boleta parezca boleta
# que tenga un mensaje de bienvenida
# luego cada productos listado de esta menera
# Prod 1---$5000
# Prod 2---$1000
# Prod 3---$2000
# Prod 4---$6000
# los totales a pagar
# Fialmente un mensaje de cierre
########TAREA########
# Tomar el CRUD de diccionario que está en este archivo
# y manipurar un diccionaario creado por usted
# puede ser cartas pokemon, autos, peliculas, series,  etc.
# Presentarlo el dia martes en la clase para revisarlo
# con el profesor.

autos={
    1:{"nombre":"Sedan", "precio": 12000000 },
    2:{"nombre":"SUV", "precio": 15000000 },
    3:{"nombre":"Convertible", "precio": 40000000 }
} 

carrito=[]
def mostrar():
    for num, prod in autos.items():
        print(f"{num}.- {prod['nombre']}  ${prod['precio']}")
    print("-"*30)
def eliminar():
    mostrar()
    # borrar_pokemon=input("Cual es el pokemon que va a liberar ?: ")
    # pokemons.remove(borrar_pokemon)
    try:
        borrar_producto=int(input("Cual es el auto que va a eliminar ?: "))
        if borrar_producto in autos:
            del autos[borrar_producto]
        else:
            print("Ese auto no existe")
    except ValueError:
        print("Debe ingresar un número válido")
def actualizar():
    mostrar()
    try:
        key=int(input("que auto desea actualizar: "))
        if key in autos:
            nombre=input("Ingrese el nombre del tipo de auto: ")
            precio=int(input("Ingrese el precio del auto: "))
            autos[key]={"nombre":nombre, "precio": precio }
            print("actualizado con exito")
        else:
            print("Ese auto no existe")
    except ValueError:
        print("ID o precio inválido")
def agregar():
    pkm=input("Ingrese el nombre del auto: ")
    try:
        nvl=int(input("Ingrese el precio del auto: "))
    except ValueError:
        print("Precio inválido, usando 0")
        nvl=0
    autos[list(autos.keys())[-1]+1]={"nombre":pkm, "precio": nvl }
def comprar():
    while True:
        mostrar()
        try:
            comprar=int(input("Cual auto desea comprar ? ( para salir, ponga 0): "))
            if comprar==0:
                break
            if comprar in autos:
                print(f"Usted ha comprado {autos[comprar]['nombre']} por un valor de {autos[comprar]['precio']}")
                carrito.append(autos[comprar])
            else:
                print("Ese auto no existe")
        except ValueError:
            print("Debe ingresar un número válido")
def boleta():
    total=0
    print("-"*30, "0", "-"*30)
    print("Bienvenido a MiAutito.com")
    print("-"*30, "0", "-"*30)
    for p in carrito:
        total+=int(p["precio"])
        print(p["nombre"],"---$", p["precio"])
    iva=total*0.19
    print("-"*30, "0", "-"*30)
    print(f"El total de su compra es {total} y el IVA es {iva}")
    print(f"El total a pagar es  {total+iva} ")
    print("Gracias por comprar en MiAutito.com")
    print("-"*30, "0", "-"*30)
def menuProductos():
    while True:
        try:
            print("1.- Agregar Auto")
            print("2.- Eliminar Auto")
            print("3.- Actualizar Auto")
            print("4.- Mostrar Auto")
            print("5.- Comprar Auto")
            print("6.- Crear Boleta (calcula IVA) y Salir")
            op=int(input("Seleccione una opcion: "))
            match op:
                case 1:
                    agregar()
                case 2:
                    eliminar()
                case 3:
                    actualizar()
                case 4:
                    mostrar()
                case 5:
                    comprar()
                case 6:
                    boleta()
                    break
                case _:
                    print("Opcion Invalida")

        except ValueError as e:
            print("Solo numeros enteros. Error",e)
menuProductos()