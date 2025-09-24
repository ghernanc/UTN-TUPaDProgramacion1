#Crear una matriz con las notas de 5 estudiantes en 3 materias.
#• Mostrar el promedio de cada estudiante.
#• Mostrar el promedio de cada materia.
# Creo una Matriz 5x3.
notas = [         
    [10, 8, 2],
    [6, 1, 9], 
    [9, 10, 6],
    [7, 4, 10],  
    [8, 9, 4],  
]

print("notas de estudiantes:")

for fila in notas: #Cada vez que entra al bucle, fila toma una lista interna.(pasa por cada estudiante.)
    for nota in fila: #entra a esa lista y saca los valores uno por uno.(pasa por cada nota de ese estudiante.)
        print (nota, end=" ") #con end = " " evito el salto de linea,en su lugar  pone un espacio, asi imprime la lista en la misma linea
    print()    #aca Si hace el salto de linea cuando cambia de estudiante. o pasa a l lista que sigue

for i in range(5):   # i recorre a los 5 estudiantes: i = 0,1,2,3,4
    suma=0           # reseteo el acumulador para el estudiante i
    for j in range(3): # j recorre las 3 notas del estudiante i: j = 0,1,2
         suma+= notas[i][j] # sumo la nota j del estudiante i al acumulador
    promedio= suma/3   # calculo el promedio de las 3 notas
    print(f"Estudiante {i+1}: {promedio:.2f}")  # muestro el promedio con 2 decimales

for j in range(3): # j recorre las 3 materias (columna 0, 1 y 2)
    suma = 0  # reinicio la suma para cada materia
    for i in range(5): # i recorre a los 5 estudiantes (fila 0..4)
        suma += notas[i][j] # sumo la nota de la materia j del estudiante i
    promedio = suma / 5  # divido por la cantidad de estudiantes
    print(f"Promedio Materia {j+1}: {promedio:.2f}") # muestro el promedio con 2 decimales


