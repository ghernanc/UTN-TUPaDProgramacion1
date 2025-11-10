#Trabajo Práctico Integrador
#Programación I
#Luis Rivera, Comisión 10
#Gustavo Campestre, Comisión 03

#Elementos Importados.
import csv
import os
import difflib

#Constante para el archivo csv
LISTA = "listado.csv"

# Creación del CSV
def crear_csv():
    if not os.path.exists(LISTA):
        with open(LISTA, "w", newline= "", encoding= "utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames= ["País", "Población", "Superficie", "Continente"])
            escritor.writeheader()

crear_csv()

#Validaciones Generales
def validar_numero(numero):

    if not numero.isdigit():
        return False
    return True

def validar_string(texto):

    if not texto.isalpha():
        return False
    return True

def obtener_listado():

    paises = []

    with open(LISTA, newline= "", encoding= "utf-8") as archivo:
        lectura = csv.DictReader(archivo)
        for item in lectura:
            paises.append({"País": item['País'], "Población": int(item['Población']), "Superficie": int(item['Superficie']), "Continente": item['Continente']})
        return paises

def existe_pais(nombre_pais):
    
    paises = obtener_listado()

    for item in paises:
        if item['País'].strip().title() == nombre_pais.strip().title():
            return True
    return False


#Validaciones para el Alta
def validar_pais(pais):
    
    if not validar_string(pais.replace(" ","")):
        print("No se permiten caractéres numéricos ni especiales!!")
        return False
    
    if existe_pais(pais):
        print("El país que quieres agregar ya existe en el listado")
        return False
    
    return True

def validar_poblacion(numero):

    if not validar_numero(numero):
        print("Los datos ingresados no son válidos. Por favor ingrese la cantidad con caractéres numéricos: ")
        return False
    else:
        numero = int(numero)

    return True

def validar_superficie(numero):

    if not validar_numero(numero):
        print("Los datos ingresados no son válidos. Por favor ingrese la superficie con caractéres numéricos: ")
        return False
    else:
        numero = int(numero)

    return True

def validar_continente():
    CONTINENTES = {
        "1": "América",
        "2": "Asia",
        "3": "Europa",
        "4": "África",
        "5": "Oceanía"
    }


    print("\nSeleccione el continente:")
    for clave, nombre in CONTINENTES.items():
        print(f"{clave}. {nombre}")
    print("-" * 40)


    opcion = input("Ingrese el número del continente: ").strip()


    while opcion not in CONTINENTES:
        opcion = input("Opción inválida. Ingrese un número entre 1 y 5: ").strip()


    continente = CONTINENTES[opcion]
    return continente


#Actualizaciones de datos
def actualizar_poblacion():

    paises = obtener_listado()

    buscar_pais = input("Que país quieres modificar?: ").strip().title()
    while not existe_pais(buscar_pais):
        print("El país que quieres buscar no existe en el listado")
        buscar_pais = input("Que país quieres modificar?: ").strip().title()

    for item in paises:
        if item['País'] == buscar_pais:
            nueva_poblacion = input("Ingrese la densidad de población: ").strip()
            while not validar_poblacion(nueva_poblacion):
                nueva_poblacion = input("Ingrese la densidad de población: ").strip()

            item['Población'] = nueva_poblacion
            poblacion = item['Población']
            print("-"*40)
            print(f"Se modificó {buscar_pais} con éxito")
            print(f"Nueva Población: {poblacion}")
            print("-"*40)
            input("Presione ENTER para continuar..")

    with open(LISTA, "w", newline= "", encoding= "utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames= ["País", "Población", "Superficie", "Continente"])
        escritor.writeheader()
        escritor.writerows(paises)

def actualizar_superficie():

    paises = obtener_listado()

    buscar_pais = input("Que país quieres modificar?: ").strip().title()
    while not existe_pais(buscar_pais):
        print("El país que quieres buscar no existe en el listado")
        buscar_pais = input("Que país quieres modificar?: ").strip().title()

    for item in paises:
        if item['País'] == buscar_pais:
            nueva_superficie = input("Ingrese la superficie en km2: ").strip()
            while not validar_superficie(nueva_superficie):
                nueva_superficie = input("Ingrese la superficie en km2: ").strip()

            item['Superficie'] = nueva_superficie
            superficie = item['Superficie']
            print("-"*40)
            print(f"Se modificó {buscar_pais} con éxito")
            print(f"Nueva Superficie: {superficie} Km2")
            print("-"*40)
            input("Presione ENTER para continuar..")

    with open(LISTA, "w", newline= "", encoding= "utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames= ["País", "Población", "Superficie", "Continente"])
        escritor.writeheader()
        escritor.writerows(paises)


#Función para mostrar todo el listado.
def mostrar_listado(paises):

    for item in paises:
        print(f"País: {item['País']:<20} | Población: {item['Población']:>12} | Superficie: {item['Superficie']:>12} | Continente: {item['Continente']:<12}")

#keys para el ordenamiento
def por_nombre(item):
    return item['País']

def por_poblacion(item):
    return item['Población']

def por_superficie(item):
    return item['Superficie']

#Ordenar por:
#Ascendente.
def nombre_ascendente(paises):

    lista_ascendente = sorted(paises, key= por_nombre)
    return lista_ascendente

def poblacion_ascendente(paises):

    lista_ascendente = sorted(paises, key= por_poblacion)
    return lista_ascendente

def superficie_ascendente(paises):

    lista_ascendente = sorted(paises, key= por_superficie)
    return lista_ascendente

#Descendente.
def nombre_descendente(paises):

    lista_descendente = sorted(paises, key= por_nombre, reverse= True)
    return lista_descendente

def poblacion_descendente(paises):

    lista_descendente = sorted(paises, key= por_poblacion, reverse= True)
    return lista_descendente

def superficie_descendente(paises):

    lista_descendente = sorted(paises, key= por_superficie, reverse= True)
    return lista_descendente


#Filtros.
def filtrar_poblacion():
    
    print("-"*40)
    print("\nFiltrar por población:")
    print("1. Megapoblado (> 100 millones)")
    print("2. Muy poblado (51 - 100 millones)")
    print("3. Poblado medio-alto (21 - 50 millones)")
    print("4. Poblado medio (11 - 20 millones)")
    print("5. Poco poblado (1 - 10 millones)")
    print("6. Muy poco poblado (100.000 - < 1 millón)")
    print("7. Microestado (< 100.000)")
    print("8. Para buscar de forma manual.")
    print("-"*40)

    opcion = input("Ingrese una opción: (1-8): ").strip()
    print("-"*40)

    while opcion not in ("1", "2", "3", "4", "5", "6", "7", "8"):
        opcion = input("Opción inválida. Ingrese un número entre 1 y 8: ").strip()

    paises = obtener_listado()
    filtrados = []

    for item in paises:
        item['Población'] = int(item['Población'])

        if opcion == "1":
            if item['Población'] > 100000000:
                filtrados.append({"País": item['País'], "Población": item['Población']})
        elif opcion == "2":
            if item['Población'] >= 51000000 and item['Población'] <= 100000000:
                filtrados.append({"País": item['País'], "Población": item['Población']})
        elif opcion == "3":
            if item['Población'] >= 21000000 and item['Población'] < 51000000:
                filtrados.append({"País": item['País'], "Población": item['Población']})
        elif opcion == "4":
            if item['Población'] >= 11000000 and item['Población'] < 21000000:
                filtrados.append({"País": item['País'], "Población": item['Población']})
        elif opcion == "5":
            if item['Población'] >= 1000000 and item['Población'] < 11000000:
                filtrados.append({"País": item['País'], "Población": item['Población']})
        elif opcion == "6":
            if item['Población'] >= 100000 and item['Población'] < 1000000:
                filtrados.append({"País": item['País'], "Población": item['Población']})
        elif opcion == "7":
            if item['Población'] < 1000000:
                filtrados.append({"País": item['País'], "Población": item['Población']})

    if opcion == "8":
        ingreso_manual = input("Ingrese la cantidad de población: ").strip()
        while not validar_poblacion(ingreso_manual):
            ingreso_manual = input("Ingrese la cantidad de población: ").strip()

        for item in paises:
            item['Población'] = int(item['Población'])

            if int(ingreso_manual) == item['Población']:
                filtrados.append({"País": item['País'], "Población": item['Población']})
        
    if filtrados:
        print("---Países filtrados---\n")
        for item in filtrados:
            print(f"País: {item['País']} - Población: {item['Población']}")
    else:
        print("No hay países en ese rango de población")

    print("-"*40)
    input("Presione ENTER para continuar..")

def filtrar_superficie():
    
    print("-"*40)
    print("\nFiltrar por superficie (km2):")
    print("1. Gigantes / Continentales (> 3.000.000 km2)")
    print("2. Muy grandes (1.000.000 - 2.999.999 km2)")
    print("3. Grandes (500.000 - 999.999 km2)")
    print("4. Medianos (100.000 - 499.999 km2)")
    print("5. Pequeños (10.000 - 99.999 km2)")
    print("6. Muy pequeños (1.000 - 9.999 km2)")
    print("7. Microestado (< 1.000 km2)")
    print("8. Para buscar de forma manual.")
    print("-"*40)

    opcion = input("Ingrese una opción: (1-8): ").strip()
    print("-"*40)

    while opcion not in ("1", "2", "3", "4", "5", "6", "7", "8"):
        opcion = input("Opción inválida. Ingrese un número entre 1 y 8: ").strip()

    paises = obtener_listado()
    filtrados = []

    for item in paises:
        item['Superficie'] = int(item['Superficie'])

        if opcion == "1":
            if item['Superficie'] > 3_000_000:
                filtrados.append({"País": item['País'], "Superficie": item['Superficie']})
        elif opcion == "2":
            if item['Superficie'] >= 1_000_000 and item['Superficie'] <= 2_999_999:
                filtrados.append({"País": item['País'], "Superficie": item['Superficie']})
        elif opcion == "3":
            if item['Superficie'] >= 500_000 and item['Superficie'] <= 999_999:
                filtrados.append({"País": item['País'], "Superficie": item['Superficie']})
        elif opcion == "4":
            if item['Superficie'] >= 100_000 and item['Superficie'] <= 499_999:
                filtrados.append({"País": item['País'], "Superficie": item['Superficie']})
        elif opcion == "5":
            if item['Superficie'] >= 10_000 and item['Superficie'] <= 99_999:
                filtrados.append({"País": item['País'], "Superficie": item['Superficie']})
        elif opcion == "6":
            if item['Superficie'] >= 1_000 and item['Superficie'] <= 9_999:
                filtrados.append({"País": item['País'], "Superficie": item['Superficie']})
        elif opcion == "7":
            if item['Superficie'] < 1_000:
                filtrados.append({"País": item['País'], "Superficie": item['Superficie']})

    if opcion == "8":
        ingreso_manual = input("Ingrese la superficie en km2: ").strip()
        while not validar_superficie(ingreso_manual):
            ingreso_manual = input("Ingrese la superficie en km2: ").strip()

        for item in paises:
            item['Superficie'] = int(item['Superficie'])

            if int(ingreso_manual) == item['Superficie']:
                filtrados.append({"País": item['País'], "Superficie": item['Superficie']})
        
    if filtrados:
        print("---Países filtrados---\n")
        for item in filtrados:
            print(f"País: {item['País']} - Superficie: {item['Superficie']}")
    else:
        print("No hay países en ese rango de superficie")

    print("-"*40)
    input("Presione ENTER para continuar..")

def filtrar_continente():
    
    print("-"*40)
    print("\nFiltrar por Continente:")
    print("1. Países en América.")
    print("2. Países en Europa.")
    print("3. Países en Asia.")
    print("4. Países en África.")
    print("5. Países en Oceanía")
    print("-"*40)

    opcion = input("Ingrese una opción: (1-5): ").strip()
    print("-"*40)

    while opcion not in ("1", "2", "3", "4", "5"):
        opcion = input("Opción inválida. Ingrese un número entre 1 y 5: ").strip()
        print("-"*40)

    paises = obtener_listado()
    filtrados = []

    for item in paises:

        if opcion == "1":
            if item['Continente'] == "América":
                filtrados.append({"País": item['País'], "Continente": item['Continente']})
        elif opcion == "2":
            if item['Continente'] == "Europa":
                filtrados.append({"País": item['País'], "Continente": item['Continente']})
        elif opcion == "3":
            if item['Continente'] == "Asia":
                filtrados.append({"País": item['País'], "Continente": item['Continente']})
        elif opcion == "4":
            if item['Continente'] == "África":
                filtrados.append({"País": item['País'], "Continente": item['Continente']})
        elif opcion == "5":
            if item['Continente'] == "Oceanía":
                filtrados.append({"País": item['País'], "Continente": item['Continente']})
        
      
    if filtrados:
        print("---Países filtrados---\n")
        for item in filtrados:
            print(f"País: {item['País']} - Continente: {item['Continente']}")
    else:
        print("No hay países registrados en ese continente.")

    print("-"*40)
    input("Presione ENTER para continuar..")


#Estadísticas
def pais_max_poblacion(paises):
    if not paises:
        return None
    mayor = paises[0]
    for pais in paises:
        if pais["Población"] > mayor["Población"]:
            mayor = pais
    return mayor

def pais_min_poblacion(paises):
    if not paises:
        return None
    menor = paises[0]
    for pais in paises:
        if pais["Población"] < menor["Población"]:
            menor = pais
    return menor

def promedio(paises, campo):
    if not paises:
        return 0
    total = sum(pais[campo] for pais in paises)
    return total // len(paises)

def cantidad_por_continente(paises):
    conteo = {}
    for pais in paises:
        continente = pais["Continente"]
        conteo[continente] = conteo.get(continente, 0) + 1
    return conteo


#Función para dar el alta a un país con todos sus datos.
def alta_pais():

    nombre_pais = input("Ingrese el nombre del país que desea agregar: ").strip().title()
    while not validar_pais(nombre_pais):
        nombre_pais = input("Ingrese el nombre del país que desea agregar: ").strip().title()
    print("-"*40)

    poblacion_pais = input("Ingrese la densidad de población: ").strip()
    while not validar_poblacion(poblacion_pais):
        poblacion_pais = input("Ingrese la densidad de población: ").strip()
    print("-"*40)

    superficie_pais = input("Ingrese la superficie en km2: ").strip()
    while not validar_superficie(superficie_pais):
        superficie_pais = input("Ingrese la superficie en km2: ").strip()
    print("-"*40)

    nombre_continente = validar_continente()
    print("*"*40)

    with open(LISTA, "a", newline= "", encoding= "utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames= ["País", "Población", "Superficie", "Continente"])
        escritor.writerow({"País": nombre_pais, "Población": poblacion_pais, "Superficie": superficie_pais, "Continente": nombre_continente})

    print(f"Se agrego con éxito los datos del país {nombre_pais}")
    print("*"*40)
    input("Presione ENTER para continuar..")

#Función para actualizar datos de población o superficie.
def actualizar_datos():
    
    actualizacion = input("1) Para modificar la Población: \n2) Para modificar la Superficie: \n > Ingrese una opción: ").strip()

    while actualizacion != "1" and actualizacion != "2":
        print("Opción Inválida. Intente de nuevo")
        actualizacion = input("1) Para modificar la Población: \n2) Para modificar la Superficie: \n > Ingrese una opción: ").strip()

    if actualizacion == "1":
        actualizar_poblacion()

    if actualizacion == "2":
        actualizar_superficie()

#Función para buscar paises en coincidencia (literales y parciales)
def busqueda_pais():

    buscar_pais = input("Que país deseas buscar?: ").strip().title()
    while not validar_string(buscar_pais):
        print("Ingresaste un valor inválido.")
        buscar_pais = input("Que país deseas buscar?: ").strip().title()
    
    paises = obtener_listado()
    encontrado = False

    for item in paises:

        similitud = difflib.SequenceMatcher(None, item['País'].title(), buscar_pais.title()).ratio()

        if buscar_pais in item['País']:
            print(f"País: {item['País']} - Población: {item['Población']} - Superficie: {item['Superficie']} - Continente: {item['Continente']}")
            encontrado = True
            
        elif similitud > 0.7:
            print(f"País: {item['País']} - Población: {item['Población']} - Superficie: {item['Superficie']} - Continente: {item['Continente']}")
            encontrado = True

    if not encontrado:
        print("No se encontraron países que coincidan con tu búsqueda.")                    

    print("-"*40)
    input("Presione ENTER para continuar..")

#Función para filtrar.
def filtrar_por():
    
    filtrar = input("1) Para filtrar por Población: \n2) Para filtrar por Superficie: \n3) Para filtrar por Continente: \n > Ingrese una opción: ").strip()

    while filtrar != "1" and filtrar != "2" and filtrar != "3":
        print("-"*40)
        print("Opción Inválida. Intente de nuevo")
        print("-"*40)
        filtrar = input("1) Para filtrar por Población: \n2) Para filtrar por Superficie: \n3) Para filtrar por Continente: \n > Ingrese una opción: ").strip()
        
    
    if filtrar == "1":
        filtrar_poblacion()

    if filtrar == "2":
        filtrar_superficie()

    if filtrar =="3":
        filtrar_continente()

#Función para ver el listado y ordenar.
def paises_ordenados_por():

    paises = obtener_listado()

    print("-"*40)
    print("Ordenar por:")
    print("1. Nombre - Ascendente (A-Z)")
    print("2. Nombre - Descendente (Z-A)")
    print("3. Población - Ascendente (menor a Mayor)")
    print("4. Población - Descendente (Mayor a menor)")
    print("5. Superficie - Ascendente (menor a Mayor)")
    print("6. Superficie - Descendente (Mayor a menor)")
    print("-"*40)

    opcion = input("Ingrese una opción: (1-6): ").strip()
    print("-"*40)

    while opcion not in ("1", "2", "3", "4", "5", "6"):
        opcion = input("Opción inválida. Ingrese un número entre 1 y 6: ").strip()

    if opcion == "1":
        ordenados = nombre_ascendente(paises)
    elif opcion == "2":
        ordenados = nombre_descendente(paises)
    elif opcion == "3":
        ordenados = poblacion_ascendente(paises)
    elif opcion == "4":
        ordenados = poblacion_descendente(paises)
    elif opcion == "5":
        ordenados = superficie_ascendente(paises)
    elif opcion == "6":
        ordenados = superficie_descendente(paises)
    else:
        print("Opción inválida.")
        return

    mostrar_listado(ordenados)
    print("*"*40)
    input("Presione ENTER para continuar..")

#Función que muestra las estadísticas.
def mostrar_estadisticas():

    paises = obtener_listado()

    while True:

        print("-"*40)
        print("\n== ESTADÍSTICAS ==")
        print("1. País con mayor población")
        print("2. País con menor población")
        print("3. Promedios")
        print("4. Cantidad por continente")
        print("0. Volver")
        print("-"*40)

        opcion = input("Ingrese una opción: ").strip()
        while opcion not in ("0", "1", "2", "3", "4"):
            opcion = input("Opción inválida. Ingrese un número entre 0 y 4: ").strip()
            print("-"*40)

        if opcion == "1":
            mayor = pais_max_poblacion(paises)
            print(f"País con mayor población: {mayor['País']} ({mayor['Población']})")
        elif opcion == "2":
            menor = pais_min_poblacion(paises)
            print(f"País con menor población: {menor['País']} ({menor['Población']})")
        elif opcion == "3":
            print(f"Promedio de población: {promedio(paises, 'Población')}")
            print(f"Promedio de superficie: {promedio(paises, 'Superficie')}")
        elif opcion == "4":
            conteo = cantidad_por_continente(paises)
            print("Cantidad de países por continente:")
            for cont, cant in conteo.items():
                print(f"- {cont}: {cant}")
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

        print("-"*40)
        input("Presione ENTER para continuar..")


#Menú de la aplicación.
def mostrar_menu():
    while True:

        menu = [
            "*"*40,
            "1. Agregar un País.",
            "2. Actualizar Datos (Población/Superficie).",
            "3. Buscar País.",
            "4. Filtrar países por.",
            "5. Lista de países (Ordenador por:).",
            "6. Ver estadísticas",
            "7. Salir",
            "*"*40
        ]

        for i in menu:
            print(i)
        
        opcion = input("Ingrese una opción: ").strip()

        match opcion:

            case "1":
                alta_pais()
                
            case "2":
                actualizar_datos()
                
            case "3":
                busqueda_pais()
                
            case "4":
                filtrar_por()
                
            case "5":
                paises_ordenados_por()
                
            case "6":
                mostrar_estadisticas()
                
            case "7":
                print("Gracias por usar la aplicación")
                break
            case _:
                print("Opción Inválida. Ingrese una opción del menú")

mostrar_menu()