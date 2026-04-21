# clave=input("Ingrese la clave: ").lower()
# if clave=="shazam":
#     print("Clave correcta")
# else:
#     print("clave incorrecta")

# nom=input("Ingrese su nombre: ")
# if len(nom)>=4 and len(nom)<=10:
#     print("su nombre esta entre los 4 y 10 caracteres")
# else:
#     print("su nombre es muy corto o muy largo, cambielo")

pin=int(input("Ingrese un pin: "))
while len(str(pin))!=4:
    pin=int(input("Ingrese otro pin: "))
print("Bien")