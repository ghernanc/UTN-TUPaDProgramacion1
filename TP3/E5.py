#5) Crea un juego en el que el usuario deba adivinar un número aleatorio 
# entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron
#  necesarios para acertar el número.


import random #importo la funcion random para poder utilizarla.

# Generar número aleatorio
numero = random.randint(0, 9) #genera un numero aleatoreo entre 0 y 9 y lo guarda en numero.

cont = 1 #Pongo en 1 para que tome el primer intento.
adivina=int(input("Intente adivinar el numero aleatorio entre 0 y 9: ")) #Pido el dato antes del ciclo para tomar el primer valor.
                                                                         #Si adivina en el primer intento no vuelve a preguntar y termina.
                                                                         #Sino, entra al ciclo y vuelve a preguntar.

while numero != adivina: #mientras el numero ingresado sea distinto, el ciclo va a volver a pedir el dato.
    cont += 1  #suma los intentos.
    adivina = int(input("Intente adivinar el numero aleatorio entre 0 y 9: "))#vuelvo a pedir otro dato ya dentro del ciclo.



print("¡Adivino! El numero era:", numero, "y la cantidad de intentos fue:", cont)



