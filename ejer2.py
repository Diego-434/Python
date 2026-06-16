#Gestor de pacientes
pacientes=[
    {"nombre": "Aquiles Bravo", "prevision": "Fonasa", "temperatura": 34.6, "grave": False}

]

def mostrar():
    print(pacientes)
def ingresar():
    nom=input("Ingrese el nombre del paciente: ")
    pre=input("Ingrese la prevision del paciente (Fonasa, Isapre o Fodesa): ")
    while pre.lower() != "fonasa" or pre.lower() != "isapre" or pre.lower() != "fodesa":
        pre=input("Ingrese la prevision del paciente (Fonasa, Isapre o Fodesa): ")
    while True:
        try:
            tem=float(input("Ingrese la temperatura del paciente: "))
            break
        except ValueError:
            print("Solo numeros")
    if tem>=39:
        gr=True
    else:
       gr=False
    pacientes.append({"nombre": nom, "prevision": pre, "temperatura": tem, "grave": gr}) 

ingresar()
mostrar()