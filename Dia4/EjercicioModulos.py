from mismodulos import *

nombres = [
    ["Adrián"],
    ["Alejandra"],
    ["Ámbar", "Isabella"],
    ["Andrés", "David"],
    ["Aura", "Camila"],
    ["Camilo", "Andrés"],
    ["Daniel", "Esteban"],
    ["David", "Santiago"],
    ["Edgar", "Leonardo"],
    ["Gerson", "Steven"],
    ["Harley", "Yefrey"],
    ["John", "Stiven"],
    ["Juan", "David"],
    ["Juan", "David"],
    ["Juan", "David"],
    ["Juan", "Eduardo"],
    ["Juan", "Fernando"],
    ["Juan", "Jose"],
    ["Maria", "Juliana"],
    ["Mateo", "Roman"],
    ["Naya", "Zarela"],
    ["Nicolas"],
    ["Omar", "Fernando"],
    ["Santiago"],
    ["Santiago", "Andrés"],
    ["Santiago"],
    ["Sara", "Sofía"],
    ["Sayara", "Yurley"],
    ["Sergio", "Andrés"],
    ["Simón", "Dante"],
    ["Thomas", "Sebastián"],
    ["Vladimir"]
]

apellidos = [
    ["Quintero", "Pinzón"],
    ["Pinzón", "Alvarez"],
    ["Plata", "López"],
    ["Reyes", "Espinel"],
    ["Pico", "Araque"],
    ["Suárez", "Fuentes"],
    ["Guerrero", "Quintero"],
    ["Vera", "Mendez"],
    ["Acevedo", "Arteaga"],
    ["Chaparro", "Martínez"],
    ["Cabrales", "Vargas"],
    ["Negron", "Regalado"],
    ["Saavedra", "Jaimez"],
    ["Santoyo", "Jaimes"],
    ["Vargas", "Soto"],
    ["Pinilla", "Guzmán"],
    ["Umaña", "Barragan"],
    ["Abril", "Roman"],
    ["Saavedra", "Mejia"],
    ["Camargo"],
    ["Lizcano", "Jaimes"],
    ["Chedraui", "Mantilla"],
    ["Granados", "Parra"],
    ["Aguilar", "Vesga"],
    ["Quiñonez", "Sosa"],
    ["Jaimes", "Perez"],
    ["Díaz", "Rodríguez"],
    ["Aparicio", "Arciniegas"],
    ["Rueda", "Hernández"],
    ["Salamanca", "Galvis"],
    ["Bastos", "Garcia"],
    ["Diaz", "Contreras"]
]

boolea = True
while (boolea == True ):

    
    print("\nBienvenido al sistema de listas")
    print("Que te gustaría hacer?")
    print("1.Editar nombre y apellido")
    print("2.Agregar estudiante")
    print("3.Eliminar estudiante")
    print("4.Salir")
    opcion=int(input(":"))
    if(opcion == 1):
        print("listadeestudiantes")
        lista( nombres, apellidos)
        nombreEstudiante=int(input(" A Cual estudiante quieres editarle el nombre ? (numero):"))
        nombreEstudianteNuevo=input("Cual será el nombre nuevo del estudiante?:")
        apellidoEstudianteNuevo=input("Cual será el apellido nuevo del estudiante?:")
        editrest (nombres,nombreEstudiante,nombreEstudianteNuevo,apellidos,apellidoEstudianteNuevo)
        print("listadeestudiantes")
        lista( nombres,apellidos)
    elif (opcion == 2):
         print("listadeestudiantes")
         lista( nombres,apellidos)
         agest=(input("Escribe el nombre de estudiante que quieres agregar"))
         apes=(input("Escribe el apellido de estudiante que quieres agregar"))
         ag (nombres,agest,apellidos, apes)
         print("listadeestudiantes")
         lista( nombres, apellidos)
    elif  (opcion==3):
         print("listadeestudiantes")
         lista( nombres, apellidos)
         deles=int(input("Ecriba el numero del estudiante que deea eliminar"))
         del nombres[deles-1]
         del apellidos[deles-1] 
         print("listadeestudiantes")
         lista( nombres, apellidos)
    elif (opcion==4 ): 
         fin(boolea)

