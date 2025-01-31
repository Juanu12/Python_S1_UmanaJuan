def temperatura1 (a):
   b = ((a * 9/5)+ 32)
   return b
def temperatura2 (b):
   a = ( (b - 32) * 5/9)
   return a

temp=float(input("Ingrese una temperatura"))
op=str(input("Ingrese si su temperatura esta en Celcius(1) o Fahrenheit(2)"))

if op == "1":
   print("La conversion de Celcius a Fahrenheit es",temperatura1(temp))
   if op == "2":
      print("La conversion de Fahrenheit a Celcius es",temperatura2(temp))
elif op != 1 or op != 2 :
 print("Numero ingresado no es correcto")

   


