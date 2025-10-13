
# tp7_ejercicio7.py
# Objetivo: Dados dos conjuntos (sets) de estudiantes que aprobaron Parcial 1 y Parcial 2,
#           mostrar:
#           - Los que aprobaron ambos parciales (intersección).
#           - Los que aprobaron solo uno (diferencia simétrica).
#           - Los que aprobaron al menos uno (unión).

# Pedimos listas de nombres separadas por coma para cada parcial.
p1_input = input('Ingresá nombres que aprobaron Parcial 1 (separados por coma): ').strip()
p2_input = input('Ingresá nombres que aprobaron Parcial 2 (separados por coma): ').strip()

# Convertimos a sets quitando espacios en blanco alrededor de cada nombre.
set_p1 = {n.strip() for n in p1_input.split(',') if n.strip()}
set_p2 = {n.strip() for n in p2_input.split(',') if n.strip()}

# Intersección: quienes están en ambos conjuntos.
ambos = set_p1.intersection(set_p2)

# Diferencia simétrica: quienes están en uno u otro, pero no en ambos.
solo_uno = set_p1.symmetric_difference(set_p2)

# Unión: quienes están en al menos uno de los conjuntos.
al_menos_uno = set_p1.union(set_p2)

# Mostramos los resultados.
print('Aprobaron ambos:', sorted(ambos))
print('Aprobaron solo uno:', sorted(solo_uno))
print('Aprobaron al menos uno:', sorted(al_menos_uno))
