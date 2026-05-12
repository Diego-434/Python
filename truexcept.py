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
while True:
    try:
        num=int(input("INGRESE la cant de notas: "))
        break
    except:
        print("Solo numeros enteros")
suma=0
for i in range (num):
    while True:
        try:
            nota=float(input(f"Ingrese la nota {i+1}: "))
            break
        except ValueError:
            print("Solo numeros decimales")
    suma=suma+nota
prom=suma/num
print("el promedio es", prom)
if prom>=4:
    print("el alumno aprob")
else:
    print("el alumno reprobo")