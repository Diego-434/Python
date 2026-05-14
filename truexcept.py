# while True:
#     try:
#         num=int(input("Ingrese un numero: "))
#         break
#     except ValueError as er:
#         print(f"error {er}")
#         print("Solo debe ingresar numeros enteros estupidoo ")
# while True:
#     try:
#         num=int(input("INGRESE la cant de notas: "))
#     except ValueError as e:
#         print("Error", e)
        
#     suma=0
#     for i in range (num):
#         try:
#             nota=float(input("Ingrese la nota: "))
#         except ValueError as a:
#             print("Error", a)
#             continue
#         suma=suma+nota
#     prom=suma/num
#     print("el promedio es", prom)
#     if prom>=4:
#         print("el alumno aprob")
#     else:
#         print("el alumno reprobo")
# while True:
#     try:
#         num=int(input("INGRESE la cant de notas: "))
#         break
#     except:
#         print("Solo numeros enteros")
# suma=0
# for i in range (num):
#     while True:
#         try:
#             nota=float(input(f"Ingrese la nota {i+1}: "))
#             break
#         except ValueError:
#             print("Solo numeros decimales")
#     suma=suma+nota
# prom=suma/num
# print("el promedio es", prom)
# if prom>=4:
#     print("el alumno aprob")
# else:
#     print("el alumno reprobo")

op=0
saldo=100000
while op!=4:
    print("1. Ver mi Saldo")
    print("2. Retirar Dinero")
    print("3. Depositar Dinero")
    print("4. Salir")
    op=int(input("Seleccione una opción: "))
    match op:
        case 1:
            print(f"su saldo es de: ${saldo}")
        case 2:
            print("solo se puede sacar multiplos de $5.000")
            try:
                ret=int(input("Cuanto desea retirar?: "))
                while ret%5000!=0 or ret<0 or saldo-ret<0:
                    ret=int(input("El valor no es multiplo de 5.000 o es invalido, ingrese otro: "))
            except ValueError:
                print("Valor invalido")
                continue
            saldo=saldo-ret
            print(f"retita ${ret}, muy bien")
        case 3:
            print("solo se puede depositar multiplos de $5.000")
            try:
                dep=int(input("Cuanto desea retirar?: "))
                while dep%5000!=0 or dep<0:
                    dep=int(input("El valor no es multiplo de 5.000 o es invalido, ingrese otro: "))
            except ValueError:
                print("Valor invalido")
                continue
            saldo=saldo+dep
            print(f"Deposita ${dep}, muy bien")
        case 4:
            print("Adios")
        case _:
            print("Opcion invalida")