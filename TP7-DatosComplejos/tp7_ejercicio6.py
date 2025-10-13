
# tp7_ejercicio6.py
# Objetivo: Ingresar los nombres de 3 alumnos y, para cada uno, una tupla de 3 notas.
#           Luego, mostrar el promedio de cada alumno.

# Diccionario para guardar: nombre -> tupla de 3 notas
alumnos = {}

# Repetimos el proceso para 3 alumnos.
for i in range(3):
    # Solicitamos el nombre del alumno.
    nombre = input(f'Nombre del alumno {i+1}: ').strip()
    # Solicitamos tres notas separadas por espacios.
    notas_str = input(f'Ingresá 3 notas de {nombre} separadas por espacios: ').strip()
    # Convertimos las notas a enteros o flotantes (elegimos float para mayor precisión).
    notas_lista = [float(x) for x in notas_str.split()[:3]]
    # Si el usuario ingresó menos de 3, completamos con 0.0 (control básico).
    while len(notas_lista) < 3:
        notas_lista.append(0.0)
    # Guardamos como tupla inmutable.
    alumnos[nombre] = tuple(notas_lista[:3])

# Mostramos el promedio de cada alumno.
print('-' * 40)
for nombre, notas in alumnos.items():
    # Calculamos promedio sumando y dividiendo por la cantidad de notas.
    promedio = sum(notas) / len(notas)
    # Mostramos el resultado con 2 decimales.
    print(f'{nombre}: notas={notas}, promedio={promedio:.2f}')
