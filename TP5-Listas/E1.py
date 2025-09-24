#1) Crear una lista con las notas de 10 estudiantes.
#• Mostrar la lista completa.
#• Calcular y mostrar el promedio.
#• Indicar la nota más alta y la más baja

estudiantes = ["Mario","Laura","Juan","Luz","Pedro","Ramiro","Luis","Uma","Javier","Camila"]
notas=[6,3,6.5,9,10,10,9,10,8,7] #Creo dos  listas de 10 elementos cada una.
suma=0
promedio=0
nota_max=notas[0] #Guardo en las variable el primer valor de la lista
nota_min=notas[0] #Para luego comparar el max y min.


print("Las notas de los estudiantes son:")
for i in range(len(estudiantes)):  # recorro por indice con la funcion len
                                   # con len obtengo el tamaño de la lista y se usa en range.
    print(estudiantes[i], "→", notas[i]) #imprimo el contenido de i , en ambas listas secuencialmente.
    suma += notas[i] # sumo solo el valor que contiene i


#la primera nota es al inicio tanto el maximo como el minimo, y luogo el bucle va comparando y actualizando segun corresponda.
    if notas[i] > nota_max:  # comparo la nota
        nota_max = notas[i]  # si es mayor la guardo
    if notas[i] < nota_min:  # comparo la nota
        nota_min = notas[i]  # si es menor la guardo


promedio=suma/len(notas)   # la funcion len calcula el tamaño de la lista
                           # Luego lo divido por la suma total
                           # y obtengo el promedio.   
print("Y el promedio de las notas  es: ", promedio) 
print("La nota mas alta es: ",nota_max) 
print("La nota mas baja  es: ",nota_min)  


