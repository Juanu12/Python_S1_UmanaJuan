##Algoritmo para calcular si dos numeros son amigos
amigo1= int(input("Escriba el numero amigo 1"))
amigo2 = int(input("Escribe el numero amigo 2"))
suma1=0
suma2=0
for i in range (1,amigo1):
    if amigo1%i == 0:
             suma1 == suma1 +i
for i in range (1,amigo2):
    if amigo2%i == 0:
            suma2 == suma2 +i
if suma1 == suma2 and suma2 == suma1:
                  print("Los numeros son amigos")
else:
                  print("Los numeros no son amigos")
 ##Ejercicio desarrollado por Juan Umaña/ Ti 1097783757