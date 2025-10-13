
# tp7_ejercicio5.py
# Objetivo: Dada una frase ingresada por el usuario, imprimir:
#   - El conjunto de palabras únicas (set).
#   - Un diccionario con el conteo de ocurrencias de cada palabra.

# Solicitamos una frase al usuario.
frase = input('Ingresá una frase: ').strip()

# Normalizamos la frase a minúsculas para contar de forma consistente.
frase_normalizada = frase.lower()

# Separamos la frase en palabras usando split por espacios.
palabras = frase_normalizada.split()

# Obtenemos las palabras únicas usando un set (no permite repetidos).
palabras_unicas = set(palabras)

# Creamos un diccionario para contar ocurrencias de cada palabra.
conteo = {}
for p in palabras:
    # Si la palabra no está en el diccionario, inicializamos el contador en 0.
    if p not in conteo:
        conteo[p] = 0
    # Incrementamos el contador para la palabra p.
    conteo[p] += 1

# Mostramos los resultados.
print('Palabras únicas (set):', palabras_unicas)
print('Conteo de palabras (dict):', conteo)
