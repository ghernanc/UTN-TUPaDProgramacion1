# Ejercicio 8 - Calcular el IMC (Índice de Masa Corporal).

def calcular_imc(peso, altura):  # Definimos la función con dos parámetros.
    # En Python los parámetros se pasan por referencia a objetos.
    # En este caso usamos números (tipos inmutables), por lo que se comportan como pasados por valor.
    # Verificamos que la altura sea válida.
    if altura <= 0:
        raise ValueError("La altura debe ser mayor que cero.")  #raise(palabra clave del lenguaje Python igual que if, for, def, return, etc) 
                                                                #se usa para lanzar un error (excepción) de forma manual.
                                                                #Sirve cuando querés detener el programa si ocurre una situación 
                                                                #incorrecta o inesperada.
    # Fórmula: peso / (altura al cuadrado).
    return peso / (altura ** 2)

# Solicitamos al usuario los datos necesarios.
# Usamos float() porque se pueden ingresar valores decimales.
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

# Calculamos el IMC llamando a la función y mostramos el resultado con dos decimales.
# f crea una f-string, { } insertan variables y .2f limita el resultado a 2 decimales.
print(f"Su IMC es: {calcular_imc(peso, altura):.2f}")
