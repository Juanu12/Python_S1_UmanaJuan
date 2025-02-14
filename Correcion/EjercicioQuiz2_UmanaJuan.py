import json
def abrirJSON():
    dicFinal={}
    with open('./diccionario.json','r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./diccionario.json",'w') as outFile:
        json.dump(dic,outFile)
from datetime import datetime
inmuebles={}

inmuebles=abrirJSON()

inmueblesGeneral = {}
inmueblesGeneral = abrirJSON

print("\nBienvenido al programa de Busqueda de innmuebles")
print("¿Eres cliente o administrador? (1/2)")
per = int (input(":"))
if per == 1:
 pass

else:  
    (per == 2)
    clave = int (input("digite su clave"))
    if clave == 1234:
        print("Que te gustaría hacer?")
        print("#######################")
        print("1.Agregar inmueble")
        print("#######################")
        print("2. Ver inmuebles")
        print("#######################")   
        print("3.Editar inmuebles")
        print("#######################")
        print("4.Eliminar inmuebles")
        print("#######################")
        print("5.Salir del programa")
        op = (input("Elija una opción "))
        if op == "1":
            inmuebleNuevo = {}
            zonaNuevo = input("Zona A/B:")
            inmuebleNuevo["zona"] = zonaNuevo
            anoNuevo = int(input("Año Construcción:"))
            inmuebleNuevo["Epoca"] = anoNuevo
            metrosNuevo = int(input("Metros Construidos:"))
            inmuebleNuevo["metros"] = metrosNuevo
            habitacionesNuevo = int(input("Habitaciones:"))
            inmuebleNuevo["habitaciones"] = habitacionesNuevo
            garajeNuevo = int(input("¿Tiene garaje?(Si=1,No=0):"))
            if(garajeNuevo == 1):
                garaje = 1
                inmuebleNuevo["garaje"] = True
            else:
                garaje = 0
                inmuebleNuevo["garaje"] = False
            if(inmuebleNuevo["zona"] == "A"):
                current_year = datetime.now().year
                precioFinalA = ((inmuebleNuevo["metros"]) * 1000 + (inmuebleNuevo["habitaciones"]) * 5000 + garaje * 15000) * (1 - (current_year - inmuebleNuevo["año"]) / 100)
                inmuebleNuevo["precio"] = precioFinalA
            else:
                current_year = datetime.now().year
                precioFinalB = ((inmuebleNuevo["metros"]) * 1000 + (inmuebleNuevo["habitaciones"]) * 5000 + garaje * 15000) * (1 - (current_year - inmuebleNuevo["año"]) / 100) * 1.5
                inmuebleNuevo["precio"] = precioFinalB
            print("\n#########################")
            print("###Inmueble Nuevo ##")
            print("#########################")
            print("Zona:", inmuebleNuevo["zona"])
            print("Año de construcción:", inmuebleNuevo["año"])
            print("Tamaño:", inmuebleNuevo["metros"], "m2")
            print("Habitaciones:", inmuebleNuevo["habitaciones"])
            if(inmuebleNuevo["garaje"] == True):
                garaje = 1
                print("Garaje: Disponible")
            else:
                garaje = 0
                print("Garaje: No disponible")
            print("Precio:", inmuebleNuevo["precio"])
            inmueblesGeneral["inmuebles"].append(inmuebleNuevo)
            guardarJSON(inmueblesGeneral)
        else:
         print("Clave incorrecta")
         if op == "2":
            print ("Inmuebles disponibles")
            for i in range(len(inmuebles["inmuebles"])):
             print("\nVivienda #",i+1)
             print("Zona:",inmuebles["inmuebles"][i]["zona"])
             print("Año de construcción:",inmuebles["inmuebles"][i]["Epoca"])
             print("Tamaño:",inmuebles["inmuebles"][i]["metros"],"m2")
             print("Habitaciones:",inmuebles["inmuebles"][i]["habitaciones"])
        if(inmuebles["inmuebles"][i]["garaje"]==True):
            

         inmuebles=abrirJSON()
