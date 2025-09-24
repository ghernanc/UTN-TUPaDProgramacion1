#Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
#semana.
#• Calcular el promedio de las mínimas y el de las máximas.
#• Mostrar en qué día se registró la mayor amplitud térmica.

# Creo una Matriz 7x2: [min, max] por dia .
temps = [         
    [10, 18],  # Lunes
    [12, 23],  # Martes
    [9,  20],  # Miércoles
    [11, 24],  # Jueves
    [8,  19],  # Viernes
    [7,  22],  # Sábado
    [13, 25],  # Domingo
]

#Creo una lista que contenga todos los dias para luego usarla
dias = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]

#creo dos listas
mins = []
maxs = []
                          #fila es la variable de iteracion del bucle.En cada vuelta del for, fila toma uno de los elementos de temps
for fila in temps:        #recorro cada fila [min, max] de la matriz temps
    mins.append(fila[0])  #tomo la minima(indice 0) y la agrego a mins
    maxs.append(fila[1])  #tomo la maxima (indice 1) y la agrego a maxs

# saco los promedios minimos con la funcion suma que suma todos los elementos de la 
# lista mins y los divido  usando la cantidad de elementos, usando la funcion len, que contiene la lista mins .
#hago lo mismo para los promedios maximos.
prom_min = sum(mins) / len(mins) 
prom_max = sum(maxs) / len(maxs)

# Amplitud tremica por dia
amplitudes = []  #creo una lista vacia
for fila in temps:              #recorro cada fila [min, max] de la matriz temps
    diferencia = fila[1] - fila[0] #tomo la diferencia que hay entre lo que contiene el indice 0 y el 1
    amplitudes.append(diferencia) # y las voy guardando en la lista nueva


# indice del dia con mayor amplitud (si hay empate, toma el primero)
idx_max_amp = 0  #creo la variable para mayor amplitud en 0
max_amp = amplitudes[0] #guardo en la variable el valor de indice 0 como el maximo hasta ahora

for i in range(1, len(amplitudes)):  #recorro desde el segundo elemento (indice 1") hasta el final
    if amplitudes[i] > max_amp:  #si i (que es lo que contiene el indice 1) es mayor  max_amp (que era lo guardado del indice 0) 
        max_amp = amplitudes[i] # entonces lo guardo
        idx_max_amp = i # lo guardo aqui tambien para identificar que die fue luego cuando imprima

#fianalmente imprimo los resultados 
print(f"Promedio de mínimas: {prom_min:.2f}°C") #con :.2f imprime el valore redondeado con 2 decimales. En una fstring {} marca el lugar donde se inserta ek valor  
print(f"Promedio de máximas: {prom_max:.2f}°C")
print(f"Mayor amplitud térmica: {amplitudes[idx_max_amp]}°C el {dias[idx_max_amp]}")#en ambas listas, amplitud y dias, busco lo que se guardo del indice e imprimo
