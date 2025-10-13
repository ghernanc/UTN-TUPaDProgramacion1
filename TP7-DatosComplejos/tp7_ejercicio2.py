
# tp7_ejercicio2.py
# Objetivo: Actualizar precios de frutas en el diccionario que resulta del punto 1.
#           Este script es autónomo: reconstruye el estado resultante del punto 1
#           y luego aplica las actualizaciones de precio.

# Estado resultante del ejercicio 1 (diccionario ya con las frutas agregadas).
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1500,
    'Pera': 2300
}

# Actualizamos los precios según lo pedido.
precios_frutas['Banana'] = 1330  # Actualizamos Banana a 1330
precios_frutas['Manzana'] = 1700 # Actualizamos Manzana a 1700
precios_frutas['Melón']  = 2800  # Actualizamos Melón a 2800

# Mostramos el diccionario resultante para verificar los cambios.
print('Precios de frutas tras actualización:', precios_frutas)
