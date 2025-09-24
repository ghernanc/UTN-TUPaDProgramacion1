#5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#• Mostrar la lista final actualizada.

estudiantes = ["Mario Pena","Laura Luque","Juan Cruz","Luz Lo","Pedro Mas","Ramiro Cadel","Luis Sexto","Uma Soler"]

print("¿Quiere agregar o eliminar estudiantes de la lista?")
print("Ingrese 'a' para agregar, 'e' para eliminar, o cualquier otra tecla para salir")

rta = input("Respuesta: ") #Espera por una respuesta y se le asigna a la variable rta

while rta in ("a", "e"): #miestras se ingrese la letra "a" y "e" se le asigna una de las dos a la variavle rta e ingreso el bucle
    if rta == "e":  #si la variable rta  contiene "e"
        nombre = input("Ingrese el nombre y apellido a eliminar: ") # ingreso el nombre que quielo eliminar y se lo asigno a la varible nombre.
        if nombre in estudiantes: # veo si lo que tiene la variable nombre esta en la lista
            estudiantes.remove(nombre)# si está lo elimino
            print(nombre, "eliminado.") # imprimo lo que se eliminó
        else:
            print("Ese estudiante no está en la lista.") # sino, lo que se asigno a la variable nombre no esta en la lista estiduates doy este mensaje.
    else:  # sino es "e" es "a" 
        nombre = input("Ingrese el nombre y apellido para agregar: ") #leo con input y lo guardo en la variable nombre
        estudiantes.append(nombre)#con append agrego lo que tiene la variable nombre a al final de la lista
        print(nombre, "agregado.")#imprimo lo agregado, osea lo que contiene la variable nombre
    

    print("Lista actualizada:", estudiantes)  #Vuelve a Esperar por una respuesta y se le asigna a la variable rta
    print("¿Quiere seguir? (a=agregar, e=eliminar, otra tecla=salir)")
    rta = input("Respuesta: ") #Vuelve a Esperar por una respuesta y se le asigna a la variable rta

print("Lista final:", estudiantes) #aca ya salio del bucle e  imprime la lista final
