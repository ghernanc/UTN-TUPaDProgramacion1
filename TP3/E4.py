#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.
print("Ingrese numeros enteros y se sumaran. Para finalizar ingrese 0.")

numero = int(input("Ingrese el primer numero: "))#pregunto afuera del ciclo para tomar el primer dato.

suma=0
while numero!=0 : #Mientras sea distinto de 0.
  suma += numero  #Lo sumo a la variable suma.
  numero = int(input("Ingrese el primer numero: ")) #Pregunto de nuevo porque  ya que estoy en el ciclo.

print("La suma es igual a: ", suma )

