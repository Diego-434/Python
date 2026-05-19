# op=0
# ind=0
# est=0
# pir=0
# cla_e=0
# cla_12=0
# cla_m=0
# ju=int(input("Ingrese la cantidad de juegos: "))
# for i in range(ju):
#     try:
#         nom=input("Cual es el nombre del juego? (minimo 5 caracteres, no se cuentan espacios): ").replace(" ","")
#         while len(nom)<=5:
#             nom=input("Texto invalido, cual es el nombre del juego? (minimo 5 caracteres, no se cuentan espacios): ").replace(" ","") 
#     except ValueError:
#         print("Valor invalido ")
#         continue
#     try:
#         pre=int(input(f"Ingrese el precio de {nom}: "))
#         while pre<0:
#             pre=int(input(f"Valor menor a 0, imposible, ingrese el precio de {nom}: "))
#     except:
#         print("Valor invalido ")
#         continue
#     if pre>20000 and pre<40000:
#         ind+=1
#     elif pre>=40000:
#         est+=1
#     elif pre>=20000:
#         pir+=1
                              
# usar if en vez de match
#     try:
#         print("1.-Clasificacion E, todos (<12)")
#         print("2.-Clasificacion +12, adolescentes (+12)")
#         print("3.-Clasificacion M, mayores de 18 (+18)")
#         op=int(input())

#         break
#     except ValueError:
#         print("Valor invalido")
#     match op:
#         case 1:
#             print(f"{nom} es clasificacion E")
#             cla_e+=1
#         case 2:
#             print(f"{nom} es clasificacion +12")
#             cla_12+=1
#         case 3:
#             print(f"{nom} es clasificacion M")
#             cla_m+=1
# print(f"Hay {pir} piratas, {ind} indies y {est} de estudio.\nClasificacion, {cla_e} para todos, {cla_12} de +12 y {cla_m} de +18")

cre=-100000
