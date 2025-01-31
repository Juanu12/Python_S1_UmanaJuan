## Formula n cantidad de terminos
sumatoria = 0
cantidaddeterminos= int (input("Escribe un termino)"))
for i in range (1,cantidaddeterminos + 1):
    if i %2 == 0: 
        sumatoria = sumatoria - (1/i)
    else: 
        sumatoria = sumatoria + (1/i)

(print("La cantidad de términos es", sumatoria))
  ##Ejercicio desarrollado por Juan Umaña/ Ti 1097783757
