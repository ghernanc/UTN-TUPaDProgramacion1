
# tp7_ejercicio10.py
# Objetivo: Dado un diccionario país -> capital, construir uno nuevo invertido
#           donde las capitales sean las claves y los países los valores.

# Diccionario de ejemplo con países y sus capitales.
pais_a_capital = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago',
    'Uruguay': 'Montevideo',
    'Paraguay': 'Asunción'
}

# Diccionario invertido: capital -> país
capital_a_pais = {}

# Recorremos pares (pais, capital) para invertirlos.
for pais, capital in pais_a_capital.items():
    # Asignamos capital como clave y pais como valor en el nuevo diccionario.
    # Nota: si existiera una capital repetida (poco probable), la última sobreescribe.
    capital_a_pais[capital] = pais

# Mostramos ambos diccionarios para verificar el resultado.
print('País -> Capital:', pais_a_capital)
print('Capital -> País:', capital_a_pais)
