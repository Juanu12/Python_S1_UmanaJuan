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
        for i in range (len(nombres)):
         nombrecompleto = " ".join(nombres[i]) + " " + " ".join(apellidos[i])
         print (f"{i+1}. {nombrecompleto}")
        nombreEstudiante=int(input(" A Cual estudiante quieres editarle el nombre ? (numero):"))
        nombreEstudianteNuevo=input("Cual será el nombre nuevo del estudiante?:")
        apellidoEstudianteNuevo=input("Cual será el apellido nuevo del estudiante?:")
        nombres[nombreEstudiante-1]=nombreEstudianteNuevo
        apellidos[nombreEstudiante-1]=apellidoEstudianteNuevo
        print(nombrecompleto," ")

    if (opcion == 2):
        for i in range (len(nombres)):
          nombrecompleto = " ".join(nombres[i]) + " " + " ".join(apellidos[i])
          print (f"{i+1}. {nombrecompleto}")
        agest=(input("Escribe el nombre de estudiante quequieres agregar"))
        apes=(input("Escribe el apellido de estudiante quequieres agregar"))
        nombres.append(agest)
        apellidos.append(apes)
        print (nombrecompleto)
    if  (opcion==3):
        for i in range (len(nombres)):
          nombrecompleto = " ".join(nombres[i]) + " " + " ".join(apellidos[i])
          print (f"{i+1}. {nombrecompleto}")
        deles=int(input("Ecriba el numero del estudiante que deea eliminar"))
        del nombres[deles-1]
        del apellidos[deles-1] 
    if (opcion==4 ): 
        boolea =False
        break
           

