#Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
#• Inicializarlo con guiones "-" representando casillas vacías.
#• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
#• Mostrar el tablero después de cada jugada.

tablero = []                            # Creamos una lista vacía que será nuestro tablero

for i in range(3):                      # Recorremos 3 veces (filas)
    fila = []                           # Creamos una lista vacía para cada fila
    for j in range(3):                  # Recorremos 3 veces (columnas)
        fila.append("-")                # Agregamos un guion "-" a la fila (casilla vacía)
    tablero.append(fila)                # Una vez armada la fila, la agregamos al tablero

# Mostrar el tablero inicial en pantalla
for fila in tablero:                    # Recorremos cada fila de la matriz
    for celda in fila:                  # Recorremos cada celda de la fila
        print(celda, end=" ")           # Imprimimos la celda con un espacio, sin salto de línea
    print()                             # Al terminar la fila, hacemos un salto de línea

# Variables de control
jugador = "X"                           # El primer turno será del jugador X
jugadas = 0                             # Contador de jugadas realizadas

while jugadas < 9:                      # Mientras no se hayan hecho las 9 jugadas posibles
    print(f"\nTurno del jugador {jugador}")  # Indicamos a quién le toca

    fila = int(input("Ingrese la fila (0-2):"))      # Pedimos número de fila
    columna = int(input("Ingrese la columna (0-2):"))# Pedimos número de columna

    # Validamos que la posición esté dentro del rango permitido
    if fila < 0 or fila > 2 or columna < 0 or columna > 2:
        print("Posición fuera de rango, intente de nuevo")
        continue                        # Vuelve a pedir la jugada sin contarla

    # Si la casilla está libre ("-"), colocamos la marca
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador # Colocamos la ficha del jugador en esa casilla
        jugadas += 1                     # Sumamos una jugada
    else:
        print("Casilla ocupada, intente de nuevo")
        continue                        # No pierde turno, vuelve a pedir otra posición

    # Mostrar tablero actualizado
    for fila in tablero:                # Recorremos el tablero
        for celda in fila:              # Cada celda de la fila
            print(celda, end=" ")       # Imprimimos las celdas con espacio
        print()                         # Salto de línea al terminar la fila

    # Cambiar de jugador
    if jugador == "X":                  # Si era X
        jugador = "O"                   # Pasa a O
    else:                               # Si era O
        jugador = "X"                   # Pasa a X





