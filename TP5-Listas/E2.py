#2) Pedir al usuario que cargue 5 productos en una lista.
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#• Preguntar al usuario qué producto desea eliminar y actualizar la lista.

print ("Ingrese cinco productos: ")

productos=[] #creo una lista vacia

for i in range(5): #defino ingresarle 5 productos 
    producto =input(f"Producto {i+1}: ")#con f string ingreso variables a un string con las llavez{}
                                        #i+1 porque el indice empieza en 0 y  le sumo 1 para que arranque mostsndo en 1.
    productos.append(producto)#agrego el producto a la lista productos(con s al final)

lista_ordenada=sorted(productos)#ordena la lista alfabeticamente.
print("Los porductos ingresados son:", lista_ordenada)#imprimo la lista.

eliminar = input("Ingrese el producto que desea eliminar: ") #guardo el nombre del producto.

if eliminar in lista_ordenada: #busco el producto en a lista
    lista_ordenada.remove(eliminar) #si esta, lo remuevo.
    print("\nLista actualizada de productos:") #imprimo la lista actualiza
    print(lista_ordenada)
else:
    print(f"\nEl producto '{eliminar}' no esta en la lista.") # si no esta, aviso con un mensaje.


