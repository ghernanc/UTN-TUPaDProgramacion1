# Ejercicio 2 - Función que recibe un nombre y devuelve un saludo personalizado

def saludar_usuario(nombre): # def indica que definimos una nueva función llamada 'saludar_usuario'.
                             # Entre paréntesis se escribe el parámetro 'nombre'
    return f"Hola {nombre}!" # Usamos una f-string para insertar el nombre dentro del texto
                             #'return' envía el resultado (el saludo) a quien llame la función.

# Llamada de prueba

print(saludar_usuario("Gustavo")) # Llamamos a la función y le pasamos el argumento "Gustavo" al parámetro 'nombre'.
