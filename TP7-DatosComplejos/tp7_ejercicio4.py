
# tp7_ejercicio4.py
# Objetivo: Programa "agenda telefónica" para cargar 5 contactos (nombre -> número)
#           y luego consultar el número por nombre si existe.

# Creamos un diccionario vacío para almacenar los contactos.
agenda = {}

# Pedimos al usuario que cargue 5 contactos.
for i in range(5):
    # Solicitamos el nombre del contacto.
    nombre = input(f'Ingresá el nombre del contacto {i+1}: ').strip()
    # Solicitamos el número del contacto.
    numero = input(f'Ingresá el número de {nombre}: ').strip()
    # Guardamos en el diccionario con "nombre" como clave y "numero" como valor.
    agenda[nombre] = numero

# Separador visual para la consulta.
print('-' * 40)

# Pedimos un nombre a consultar.
buscar = input('Ingresá un nombre para buscar su número: ').strip() #El método .strip() en Python se usa para eliminar los espacios en blanco 
                                                                    #(u otros caracteres específicos) al principio y al final de una cadena de texto.

# Verificamos si el nombre existe en la agenda.
if buscar in agenda:
    # Si existe, mostramos el número asociado.
    print(f'El número de {buscar} es: {agenda[buscar]}')
else:
    # Si no existe, informamos que no lo encontramos.
    print(f'No se encontró el contacto "{buscar}".')
