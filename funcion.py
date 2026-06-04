# def multiplicar():
#     n1=2
#     n2=4
#     return n1*n2
# vari=multiplicar()*2
# print(vari)

def suma(n1, n2):
    return n1 + n2
def resta(n1, n2):
    return n1 - n2
def divi(n1, n2):
    return n1 / n2
def mult(n1, n2):
    return n1 * n2

# op=0
# while True:
#     try:
#         print('''
#             1.-Sumar
#             2.-Restar
#             3.-Dividir
#             4.-Multiplicar          
#         ''')
#         op=int(input("Ingrese el numero: "))
#         match op:
#             case 1:
#                 n1=float(input("Ingrese numero 1: "))
#                 n2=float(input("Ingrese numero 2: "))
#                 print(suma(n1, n2))
#             case 2:
#                 n1=float(input("Ingrese numero 1: "))
#                 n2=float(input("Ingrese numero 2: "))
#                 print(resta(n1, n2))
#             case 3:
#                 n1=float(input("Ingrese numero 1: "))
#                 n2=float(input("Ingrese numero 2: "))
#                 print(divi(n1, n2))
#             case 4:
#                 n1=float(input("Ingrese numero 1: "))
#                 n2=float(input("Ingrese numero 2: "))
#                 print(mult(n1, n2))
#             case 5:
#                 print("Adios")
#                 break
#             case _:
#                 print("No poooooooooooooo")
#     except ValueError:
#         print("Ingresa un numero entero tonto")
        

def iva(cosa):
    return cosa*1.19
while True:
    try:
        cosa=float(input("Ingrese el precio del producto neto: "))
        break
    except:
        print("Valor no valido ingrese un numerooo")

print(f"El producto vale {iva(cosa)}")