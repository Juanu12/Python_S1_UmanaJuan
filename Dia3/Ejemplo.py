nombres=["Pedro", "Edgar", "David"]
print(len(nombres))
nombres.append("Aguilar") ## = ("Pedro", "Edgar", "David", "Aguilar")
print(nombres[-1])
## para almacenar diferentes tipos de datos a la vaz
nombres.append(True)
print(nombres)

## Agragar : append() para poner en cola
listaNueva=[]
listaNueva.append("Cajasan")
print(listaNueva)

## Extender , permite agregar una lista adicional al aque ya está

Lista1 =[1,2,3,4,5]
Lista1.extend ([7,8,9])

##Insertar indice
listaIndice= ["Rojo", "Azul"]
listaIndice.insert(1,"amarillo")
print (listaIndice)

## Reemplazar un item
listaReemplazar = ["Pedro", "Gomez]"]
listaReemplazar [1]= "Bomilla"
print(listaReemplazar)

## Eliminar el ultimo item, un item específico o todos

listaPop=["Andrés", "Camargo","David", "Pérez"]
listaPop.pop()
print(listaPop)
listaPop.pop(0)

## Contar elementos
vocales = ["a","e","i","o","u"]
apariciones = vocales.count("a")
print(apariciones)

##Ordenar

##ORDENAMIENTO
##Con solamente numeros
#Si quiero ordenar una lista de números utilizo .sort()
listaNumeros=[7,4,9,2,5,6,0]
listaNumeros.sort() ##Menor a mayor
print(listaNumeros)
listaNumeros.sort(reverse=True) ##Mayor a menor
print(listaNumeros)


print("\n##############")
print("\n##############")
#Recorrer una lista
estudiantes = [
    "Adrián Quintero Pinzón",
    "Alejandra Pinzón Alvarez",
    "Ámbar Isabella Plata López",
    "Andrés David Reyes Espinel",
    "Aura Camila Pico Araque",
    "Camilo Andrés Suárez Fuentes",
    "Daniel Esteban Guerrero Quintero",
    "David Santiago Vera Mendez",
    "Edgar Leonardo Acevedo Arteaga",
    "Gerson Steven Chaparro Martínez",
    "Harley Yefrey Cabrales Vargas",
    "John Stiven Negron Regalado",
    "Juan David Saavedra Jaimez",
    "Juan David Santoyo Jaimes",
    "Juan David Vargas Soto",
    "Juan Eduardo Pinilla Guzmán",
    "Juan Fernando Umaña Barragan",
    "Juan Jose Abril Roman",
    "Maria Juliana Saavedra Mejia",
    "Mateo Roman Camargo",
    "Naya Zarela Lizcano Jaimes",
    "Nicolas Chedraui Mantilla",
    "Omar Fernando Granados Parra",
    "Santiago Aguilar Vesga",
    "Santiago Andrés Quiñonez Sosa",
    "Santiago Jaimes Perez",
    "Sara Sofía Díaz Rodríguez",
    "Sayara Yurley Aparicio Arciniegas",
    "Sergio Andrés Rueda Hernández",
    "Simón Dante Salamanca Galvis",
    "Thomas Sebastián Bastos Garcia",
    "Vladimir Diaz Contreras"
]
##Metodo 1: Utilzar un for con indices
for i in range(len(estudiantes)):
    print("Estudiante#",i+1,": ",estudiantes[i])

print("\n##############")
print("\n##############")
##Metodo 2: Recorrerlo con un for que vaya indice por indice
for i in estudiantes:
    print(i)



    #Recorrer una lista
estudiantes = [
    "Adrián Quintero Pinzón",
    "Alejandra Pinzón Alvarez",
    "Ámbar Isabella Plata López",
    "Andrés David Reyes Espinel",
    "Aura Camila Pico Araque",
    "Camilo Andrés Suárez Fuentes",
    "Daniel Esteban Guerrero Quintero",
    "David Santiago Vera Mendez",
    "Edgar Leonardo Acevedo Arteaga",
    "Gerson Steven Chaparro Martínez",
    "Harley Yefrey Cabrales Vargas",
    "John Stiven Negron Regalado",
    "Juan David Saavedra Jaimez",
    "Juan David Santoyo Jaimes",
    "Juan David Vargas Soto",
    "Juan Eduardo Pinilla Guzmán",
    "Juan Fernando Umaña Barragan",
    "Juan Jose Abril Roman",
    "Maria Juliana Saavedra Mejia",
    "Mateo Roman Camargo",
    "Naya Zarela Lizcano Jaimes",
    "Nicolas Chedraui Mantilla",
    "Omar Fernando Granados Parra",
    "Santiago Aguilar Vesga",
    "Santiago Andrés Quiñonez Sosa",
    "Santiago Jaimes Perez",
    "Sara Sofía Díaz Rodríguez",
    "Sayara Yurley Aparicio Arciniegas",
    "Sergio Andrés Rueda Hernández",
    "Simón Dante Salamanca Galvis",
    "Thomas Sebastián Bastos Garcia",
    "Vladimir Diaz Contreras"
]

booleanito= True
while (booleanito==True):
    print("\nBienvenido al programa de lista de estudiantes")
    print("Que te gustaría hacer?")
    print("1.Agregar estudiante")
    print("2. Ver estudiantes")
    print("3.Editar estudiante")
    print("4.Eliminar estudiante")
    print("5.Salir del programa")
    opcionUsuario= int(input(":"))
    if(opcionUsuario==2):
        print("Lista estudiantes:")
        for i in range(len(estudiantes)):##Indicar cuántas veces debe recorrerlo de acuerdo al tamaño de la lista
            print("Estudiante #",i+1,": ",estudiantes[i])
    elif(opcionUsuario==5):
        booleanito== False
        break
    elif(opcionUsuario==1):
        nombreEstudiante=input("Que nombre te gustaría agregarle al estudiante:")
        estudiantes.append(nombreEstudiante)
        print("Lista nueva de estudiantes:")
        for i in range(len(estudiantes)):##Indicar cuántas veces debe recorrerlo de acuerdo al tamaño de la lista
            print("Estudiante #",i+1,": ",estudiantes[i])
    elif(opcionUsuario==3):
        print("Lista de estudiantes:")
        for i in range(len(estudiantes)):##Indicar cuántas veces debe recorrerlo de acuerdo al tamaño de la lista
            print("Estudiante #",i+1,": ",estudiantes[i])
        numeroEstudiante=int(input("Cual estudiante quieres editar?:"))
        nombreEstudianteNuevo=input("Cual será el nombre nuevo del estudiante?:")
        estudiantes[numeroEstudiante-1]=nombreEstudianteNuevo
    elif(opcionUsuario==4):
        print("Lista de estudiantes:")
        for i in range(len(estudiantes)):##Indicar cuántas veces debe recorrerlo de acuerdo al tamaño de la lista
            print("Estudiante #",i+1,": ",estudiantes[i])
        numeroEstudiante=int(input("Cual estudiante quieres eliminar?:"))
        estudiantes.pop(numeroEstudiante-1)