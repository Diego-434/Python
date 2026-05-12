# for i in range(3):
#     print("repeticion N", i+1)

#

# num=int(input("INGRESE UN NUMERO: "))
# for i in range(num):
#     print(i+1, "Hola usuario")


# num=int(input("INGRESE UN NUMERO: "))
# for i in range(10):
#     print(num, "X", i, num*i )


# num=int(input("INGRESE la cant de notas: "))
# suma=0
# for i in range (num):
#     nota=float(input("Ingrese la nota: "))
#     suma=suma+nota
# prom=suma/num
# print("el promedio es", prom)
# if prom>=4:
#     print("el alumno aprob")
# else:
#     print("el alumno reprobo")


# nombre=input ("Ingrese su nombre")
# cantLetra=0
# for i in "nombre":
#     print(i)
#     cantLetra=cantLetra+1
# print("La cantidad de caracteres es", cantLetra)

# suma=0
# cant=int(input("Cuantas notas son?: "))
# for i in range(cant):
#     nota=float(input(f"Ingrese la nota {i+1}: "))
#     suma=suma+nota
# prom=suma/cant
# print("el promedio es:",round(prom, 1))
# if prom>=4:
#     print("El alumno aprobo")
# else:
#     print("El alumno reprobo")

# nom=input("ingrese su nombre: ")
# print(f"su nombre tiene: {len(nom)} letras")

nom=input("ingrese su nombre: ")
vocal=0
cons=0
for i in nom:
    if i in "aeiou":
        vocal+=1
    elif i == " ":
        print()
    else:
        cons+=1
print(f"hay {vocal} vocales en su nombre y {cons} consonantes")