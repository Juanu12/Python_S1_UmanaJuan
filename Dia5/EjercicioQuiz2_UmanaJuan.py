import json
def abrirJSON():
    dicFinal={}
    with open('./bbdd_Fut.json','r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./bbdd_Fut.json",'w') as outFile:
        json.dump(dic,outFile)


inmuebles={}

inmuebles=abrirJSON()

print("\nBienvenido al programa de Busqueda de innmuebles")
per =(input("¿Eres cliente o administrador?"))
if per == "cliente":

    if (per == "administrador"):
       clave =(input("digite su clave"))
       if clave == "1234":
         print("Que te gustaría hacer?")
         print("1.Agregar inmueble")
         print("2. Ver inmuebles")
         print("3.Editar inmuebles")
         print("4.Eliminar inmuebles")
         print("5.Salir del programa")
         op = (input("Elija una opción "))
         if op == 1:
             
       else: print("La clave no  es válida")

inmuebles=abrirJSON()
