# Ejercicio 5 - Convertir segundos a horas.

def segundos_a_horas(segundos):  # Definimos la función con el parámetro 'segundos'.
                                 # 1 hora equivale a 3600 segundos, por eso dividimos la cantidad recibida entre 3600.
    return segundos / 3600  # Devuelve el resultado en horas.

# Solicitamos al usuario que ingrese la cantidad de segundos y convertimos el valor a número decimal.
segundos = float(input("Ingrese la cantidad de segundos: "))

# Mostramos el resultado en horas con dos decimales.
print(f"Horas: {segundos_a_horas(segundos):.2f}") # f se usa para crear una f-string (cadena formateada) que permite insertar variables dentro del texto.
                                                  # { } se usan para indicar dónde se mostrará el valor de la variable.
                                                  # .2f se usa para mostrar el número con 2 decimales.

