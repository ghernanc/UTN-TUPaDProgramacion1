#  Gestión de Datos de Países en Python

##  Descripción del Programa
Este proyecto fue desarrollado como parte del **Trabajo Práctico Integrador (TPI)** de la materia **Programación I**, correspondiente a la **Tecnicatura Universitaria en Programación** (Modalidad a Distancia).

El sistema tiene como objetivo **gestionar información sobre países**, permitiendo realizar operaciones de **alta, modificación, búsqueda, filtrado, ordenamiento y análisis estadístico** sobre un conjunto de datos almacenados en un archivo **CSV**.

El desarrollo aplica conceptos fundamentales de **estructuras de datos** (listas y diccionarios), **modularización** con funciones, y **métodos de validación y control de errores**.  
Su diseño se basa en una arquitectura funcional, clara y comentada, que asegura una lectura comprensible del código y facilita futuras extensiones.

---

##  Instrucciones de Uso

###  Requisitos previos
- **Python 3.x** instalado en el sistema.
- Biblioteca estándar (`csv`, `os`, `difflib`) incluida por defecto en Python.
- Visual Studio Code.

###  Ejecución del programa
1. Descargar los archivos del proyecto:
   - `#Trabajo Práctico Integrador.py`
   - `listado.csv` (si no existe, el programa lo creará automáticamente).
2. Ejecutar el programa desde consola con el siguiente comando:  
   ```bash
   python3 "#Trabajo Práctico Integrador.py"
   ```
3. Ó directamente doble click sobre el `.py` y abrirá el programa en **VS Code**. Luego con el botón triangular ▶️ puede ejecutar el programa.
4. Al iniciar, se mostrará un menú principal con las opciones disponibles.

###  Menú principal
```
****************************************
1. Agregar un País.
2. Actualizar Datos (Población/Superficie).
3. Buscar País.
4. Filtrar países por.
5. Lista de países (Ordenador por:).
6. Ver estadísticas.
7. Salir
****************************************
```
Cada opción está desarrollada para interactuar con el usuario mediante entradas validadas y mensajes claros de éxito o error.

---

##  Funcionalidades Detalladas

### Alta de País
Permite agregar un nuevo país al CSV con sus datos básicos:
- Nombre
- Población
- Superficie (en km²)
- Continente

Se incluyen validaciones que evitan nombres duplicados, campos vacíos y caracteres inválidos.

### Actualización de Datos
El usuario puede actualizar la población o superficie de un país existente.  
El programa valida que el país exista y que los valores nuevos sean numéricos válidos.

### Búsqueda de País
Se pueden realizar **búsquedas exactas o parciales** por nombre, utilizando coincidencias de texto o similitud de cadenas (`difflib.SequenceMatcher`), lo que mejora la flexibilidad en los resultados.

### Filtros Personalizados
Permite visualizar países según distintos criterios:
- Por **rango de población** (de microestados a megapoblados).
- Por **rango de superficie** (de microestados a gigantes continentales).
- Por **continente** (América, Europa, Asia, África u Oceanía).

### Ordenamientos
Los países pueden ordenarse según:
- Nombre (ascendente o descendente)
- Población (mayor a menor / menor a mayor)
- Superficie (mayor a menor / menor a mayor)

Se utiliza la función `sorted()` con claves personalizadas (`key`) para definir los criterios de comparación.

### Estadísticas Generales
Incluye el cálculo de:
- País con **mayor población**
- País con **menor población**
- **Promedio de población y superficie**
- **Cantidad de países por continente**

### Persistencia de Datos
El programa gestiona la información a través del archivo **listado.csv**, garantizando que los cambios realizados se mantengan entre ejecuciones.

---

##  Ejemplos de Entradas y Salidas

### Ejemplo de Alta de País
```
Ingrese el nombre del país que desea agregar: Japón
Ingrese la densidad de población: 125800000
Ingrese la superficie en km2: 377975
Seleccione el continente:
1. América
2. Asia
3. Europa
4. África
5. Oceanía
Ingrese el número del continente: 2
****************************************
Se agregó con éxito los datos del país Japón
```

### Ejemplo de Búsqueda 
```
Que país deseas buscar?: Brasil
País: Brasil - Población: 213993437 - Superficie: 8515767 - Continente: América
```

### Ejemplo de Estadísticas
```
== ESTADÍSTICAS ==
1. País con mayor población
2. País con menor población
3. Promedios
4. Cantidad por continente
Opción: 4

Cantidad de países por continente:
- América: 3
- Europa: 2
- Asia: 1
- Oceanía: 1
- África: 1 
```

---

##  Estructuras de Datos Utilizadas
- **Listas:** para almacenar el conjunto de países y permitir su manipulación mediante iteraciones, filtrados y ordenamientos.
- **Diccionarios:** cada país se representa como un diccionario con las claves `'País'`, `'Población'`, `'Superficie'` y `'Continente'`.
- **Funciones:** una función por responsabilidad (alta, validación, búsqueda, filtro, etc.), promoviendo la modularidad del sistema.
- **CSV:** archivo externo para la persistencia y reutilización de datos.
- **Módulos csv, os, difflib:** tres módulos de la biblioteca estándar de Python.
- **Estructuras de control:** `if/else` (condiciones lógicas), `while` (para validaciones), `for` (para recorrer listas), `match` y `case` (menú principal).
- **Algoritmos:** empleados en búsqueda, ordenamiento, filtrado y cálculos estadísticos.

---

| Integrante            | Comisión | Rol           | Aportes                                                                                                |
|-----------------------|----------|---------------|--------------------------------------------------------------------------------------------------------|
| **Luis Rivera**       | 10       | Desarrollador | Estructura del programa, desarrollo de funciones principales, y depuración general.                    |
| **Gustavo Campestre** | 03       | Desarrollador | Funciones de validación, testing funcional, depuración, documentación técnica y redacción.             | 
---
