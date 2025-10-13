
# tp7_ejercicio3.py
# Objetivo: Crear una lista con únicamente los nombres de las frutas (sin precios)
#           a partir del diccionario resultante del ejercicio 2.
#           Este script es autónomo y vuelve a construir el estado del ejercicio 2.

# Reconstruimos el diccionario tal como queda tras el ejercicio 2.
precios_frutas = {
    'Banana': 1330,
    'Ananá': 2500,
    'Melón': 2800,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1700,
    'Pera': 2300
}

# Obtenemos solo las claves (los nombres de frutas) y las convertimos a lista.
lista_frutas = list(precios_frutas.keys())

# Mostramos la lista de frutas resultante.
print('Lista de frutas:', lista_frutas)
