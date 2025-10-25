# Definición de la función es_palindromo que determina si un texto es un palíndromo
def es_palindromo(texto):
    # Elimina los espacios en blanco y convierte todo a minúsculas
    # para hacer la comparación sin distinguir mayúsculas ni espacios
    s = ''.join(texto.split()).lower()
    
    # Caso base 1: si el texto tiene un solo carácter o está vacío, es un palíndromo
    if len(s) <= 1:
        return True
    
    # Caso base 2: si el primer y último carácter son distintos, no es un palíndromo
    if s[0] != s[-1]:
        return False
    
    # Caso recursivo:
    # Se llama nuevamente a la función eliminando el primer y último carácter
    # La comparación continúa con el texto "interior"
    return es_palindromo(s[1:-1])


# Bloque principal: se ejecuta solo si el archivo se corre directamente
if __name__ == "__main__":
    # Pide al usuario que ingrese una palabra o frase
    palabra = input("Ingrese una palabra o frase: ")
    
    # Llama a la función y muestra el resultado según sea palíndromo o no
    if es_palindromo(palabra):
        print("Es un palíndromo.")
    else:
        print("No es un palíndromo.")
