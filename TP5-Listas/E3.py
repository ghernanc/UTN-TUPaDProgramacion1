#3) Generar una lista con 15 números enteros al azar entre 1 y 100.
#• Crear una lista con los pares y otra con los impares.
#• Mostrar cuántos números tiene cada lista.


import random
lista=[]
listapar=[]
listaimpar=[]
contpar=0
contimpar=0
aux=0

for i in range(15):
    aux=(random.randint(0, 100))  #La función randint del módulo random genera un número entero aleatorio entre dos valores.
                                  #Guardo un entero  al azar entre 0 y 100 en aux
    lista.append(aux) #El valor de aux lo inserto en la lista lista.
    if aux % 2 == 0:  #con el operador modulo veo si el resto es 0 para saber si es par
          listapar.append(aux) # si es par lo guardo en la lista de pares
          contpar+=1 # y sumo uno al contador de pares
    else:  #si no es par es impar
          listaimpar.append(aux) #entonces lo guardo en la lista de impares
          contimpar+=1  # y sumo 1 al contador de impares

          #Imprimo todas las listas y contadores.
print("La lista de los 15 numereros es: ", lista)
print("La lista de los numeros pares es: ", listapar, " y tiene: ", contpar, "numeros" )
print("La lista de los numereros impares es: ", listaimpar, " y tiene: ", contimpar, "numeros")


