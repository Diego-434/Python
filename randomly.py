import random ; import time

# num = random.randint(1,100)
# print("Adivine el numero entre 1 y 100 ")
# print(num)
# vidas=5
# op=0
# while op!=num and vidas>0:
#     print(f"tiene {vidas} intentos")
#     op=int(input("ingrese un numero: "))
#     if op>num:
#         print("te pasaste")
#         vidas-=1
#     elif op==num:
#         print("Bien")
#     else:
#         print("el numero debe ser mayor")
#         vidas-=1
# if vidas==0:
#     print("cagaste")

print("Juego de pelea, el turno es aleatorio")

nom1=input("Ingrese el nombre del jugador 1: ")
nom2=input("Ingrese el nombre del jugador 2: ")
golpe=0
hp1=100
hp2=100
turno=random.randint(1,2)
print(turno)

while hp1>=0 and hp2>=0:

    if turno % 2 ==0:
        golpe=random.randint(7,18)
        hp2=hp2-golpe
        turno+=1
        print(f"turno de {nom1}")
        print(f"{nom1} barra hp: {hp1* "|"}")
        time.sleep(1)
        print(f"el jugador {nom1} le lanza un golpe a {nom2} le quita {golpe}hp")
        time.sleep(2)

    elif turno % 2 ==1:
        golpe=random.randint(7,18)
        hp1=hp1-golpe
        turno+=1
        print(f"turno de {nom2}")
        print(f"{nom2} barra hp: {hp2* "|"}")
        time.sleep(1)
        print(f"el jugador {nom2} le lanza un golpe a {nom1} le quita {golpe}hp")
        time.sleep(2)

if hp1>hp2:
    print(f"jugador {nom1} gano")
else:
    print(f"jugador {nom2} gano")