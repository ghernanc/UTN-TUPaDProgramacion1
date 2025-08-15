#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero1=float(input("ingrese un numero distinto de 0:"))
numero2=float(input("ingrese otro numero distinto de 0:"))

if numero1!=0  and numero2!=0:
      suma=numero1+numero2
      resta=numero1-numero2
      division=numero1/numero2
      multiplicacion=numero1*numero2
      print(f"La suma es {suma}")
      print(f"La resta es {resta}")
      print(f"La multiplicacion es {multiplicacion}")
      print(f"La division  es {division}")
else :
       print("Uno o ambos numeros son cero")

   
      