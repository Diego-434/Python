import random

# op=0
# t_pers=0
# c_pers=0
# total=0
# while op!=4:
#     print('''
#         Menu de entradas:\n
#         1.-Niño (1-17) $1.000
#         2.-Adulto (18-64) $3.000
#         3.-Adulto mayor (64 o más) $1.500
#         4.-Salir y motrar total\n''')
#     op=int(input("seleccione una opcion: "))
#     t_pers=t_pers+c_pers
#     match op:
#         case 1:
#             c_pers=int(input("Cuantas personas son (ente 1 y 10)?: "))
#             while c_pers<1 or c_pers>10:
#                 print("cantidad fuera de rango")
#                 c_pers=int(input("Cuantas personas son?: "))
#             total=(c_pers*1000*1.19)+total
#             print(f"pagando por niño: ${c_pers*1000*1.19}")

#         case 2:
#             c_pers=int(input("Cuantas personas son (ente 1 y 10)?: "))
#             while c_pers<1 or c_pers>10:
#                 print("cantidad fuera de rango")
#                 c_pers=int(input("Cuantas personas son?: "))
#             total=(c_pers*3000*1.19)+total
#             print(f"pagando por adulto: ${c_pers*3000*1.19}")
#         case 3:
#             c_pers=int(input("Cuantas personas son? (ente 1 y 10): "))
#             while c_pers<1 or c_pers>10:
#                 print("cantidad fuera de rango")
#                 c_pers=int(input("Cuantas personas son?: "))
#             total=(c_pers*1500*1.19)+total
#             print(f"pagando por adulto mayor: ${c_pers*1500*1.19}")
#         case 4:
#             print(f"Okey, total a pagar: ${total}")
#             print(f"el total de peronas es: {t_pers}")
#         case _:
#             print("Opcion invalida")
total=0
cod=random.randint(7000, 21000)
print(cod)
op=0
while op!=4:
    print("cancha vip, general o tribuna? \n1.-VIP\n2.-General\n3.-Tribuna\n4.-Salir y ver si se aplica descuento")
    op=int(input("Ingrese la opcion: "))
    match op:
        case 1:
            total=40000*1.8
            print(f"VIP, el valor es: ${total}")
        case 2:
            total=40000*1.4
            print(f"General, el valor es: ${total}")
        case 3:
            total=40000*1.2
            print(f"Tribuna, el valor es: ${total}")
        case 4:
            print("Adios")
        case _:
            print("opcion invalida")
if cod>=7000 and cod<=12000:
    total=total*0.90
    print(f"se aplico un descuento del 10%, paga ${total}")
else:
    print(f"el total a pagar es ${total}")
    
