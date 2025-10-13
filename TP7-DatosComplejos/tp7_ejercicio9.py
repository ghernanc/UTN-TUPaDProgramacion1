
# tp7_ejercicio9.py
# Objetivo: Crear una agenda donde las claves sean tuplas (día, hora) y los valores eventos.
#           Permitir consultar qué actividad hay en cierto día y hora.

# Creamos un diccionario con algunas entradas de ejemplo.
# Usamos tuplas (dia, hora) como clave porque son hashables e inmutables.
agenda = {
    ('lunes', '09:00'): 'Reunión de equipo',
    ('martes', '14:30'): 'Clase de Programación',
    ('miércoles', '18:00'): 'Gimnasio',
}

# Mostramos la agenda actual.
print('Agenda inicial:')
for clave, evento in agenda.items():
    # Cada clave es una tupla (dia, hora); la desempaquetamos.
    dia, hora = clave
    print(f' - {dia} {hora}: {evento}')

# Línea separadora visual.
print('-' * 40)

# Permitimos consultar una actividad por día y hora.
dia = input('Ingresá un día (ej: lunes, martes, miércoles...): ').strip().lower()
hora = input('Ingresá una hora (formato HH:MM): ').strip()

# Armamos la tupla clave con el formato que usa la agenda.
clave_busqueda = (dia, hora)

# Consultamos si la clave existe en el diccionario.
if clave_busqueda in agenda:
    print(f'Actividad para {dia} {hora}: {agenda[clave_busqueda]}')
else:
    print(f'No hay actividad registrada para {dia} {hora}.')
