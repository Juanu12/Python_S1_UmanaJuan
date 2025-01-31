##lista numeros 
grande = 0
pequeno = 0
for i in range (1, 11):
    N =int(input("Ingresa el numero"))
    if i == 1 :
        grande = N
        pequeno = N
    elif N > grande:
        grande = N
    elif N < pequeno:
        pequeno = N
print("el numero más grande es", grande)
print("el numero  más pequeño es", pequeno)
  
##Ejercicio desarrollado por Juan Umaña/ Ti 1097783757