dic={
    1:{"Nombre": "Uva", "precio": 2000},   
    2:{"Nombre": "Palta", "precio":4000},
    3:{"Nombre": "Pera", "precio": 3000}
}

while True:
    try:
        print('''
        1.- Agregar Producto
        2.- Mostrar Productos
        3.- Actualizar Productos
        4.- Eliminar Producto
        5.- Comprar Producto(s)
        6.-Salir
        ''')
        op=int(input("Seleccione una opcion: "))
        match op:
            case 1:
                produ=input("Ingrese el nombre del producto: ")
                precio=int(input("Ingrese el precio del producto: "))
                list(dic.keys())[-1] +1 = {"Nombre": produ, "precio": precio}
            case 2:
                print(dic)

            case 3:
                print("a")
            case 4:
                print("a")
            case 5:
                print("a")
            case 6:

                print("Saliendo")
                break
             
            case _:
                        print("Opcion no valida")
    except Exception as e:
        print("El error es ", e)