op=0
total=0
while op!=4:
    try:
        print("1.- PC $500.000")
        print("2.- LGTV  $450.000")
        print("3.- Microondas $100.000")
        print("4.- Salir")
        print("Seleccione una opcion")
        op=int(input())
    except ValueError as e:
        print("Error", e)
        print("Solo se aceptan numeros enteros")
    match op:
        case 1:
            ""