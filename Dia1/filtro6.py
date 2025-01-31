##para calcular el sueldo bruto, neto el empleado con mayor y menor sueldo
personas=int (input("Ingrese la cantidad de empleados"))
sueldomayor=0
sueldomenor=0 
totalbruto = 0
totaleps = 0 
totalpension = 0 
totalneto = 0
emnom=""
empleado1=""
empleado2=""
for i in range (personas):
    emnom=str(input("Escriba el nombre del empleado"))
    emhoras=int (input("Escriba las horas trabajadas"))
    bruto = emhoras*20000
    eps = bruto * 0.04
    pension = bruto*0.04
    neto = bruto - eps - pension 
    totalbruto = neto
    totalbruto= totalbruto + bruto
    totaleps = totaleps + eps 
    totalpension = totalpension + pension 
    totalneto = totalneto + neto
    sueldomayor = neto 
    if sueldomayor>sueldomenor:
        sueldomenor=sueldomayor
        smayor = sueldomayor
        empleado1 = emnom 
    else:
         if sueldomayor < sueldomenor:
            smenor = sueldomayor
            empleado2 = emnom
    print("Empleado:",emnom)
    print("Sueldobruto $",bruto)
    print("eps $", eps)
    print("pension $",pension)
    print("sueldoneto $",neto)


promediobruto= totalbruto/personas
promedioneto = totalneto/personas

print("Totales:")
print("Total salarios brutos$",totalbruto)
print("Total eps $",totaleps)
print("Total pension $",totalpension)
print("Total sueldoneto $",totalneto)
print("Empleado que mas gana",empleado1)
print("Empleado que menos gana",empleado2)
print("Total salarios brutos $", promediobruto)
print("Total salrios netos $",promedioneto)
##Ejercicio desarrollado por Juan Umaña/ Ti 1097783757