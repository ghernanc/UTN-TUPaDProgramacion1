#4) Dada una lista con valores repetidos:
#lista=[1,3,5,3,7,1,9,5,3]
#• Crear una nueva lista sin elementos repetidos.
#• Mostrar el resultado.

lista=[1,3,5,3,7,1,9,5,3]
sinrepetidos=[] #creo una lista vacia
for aux in lista:  #recorro la lista guardando cada contenido de cada posicion en aux
    if aux not in sinrepetidos: #uso el operador de pertenecia not in  
                                #si aux no esta en la lista, la condicino es True y se ejecuta el bloque
        sinrepetidos.append(aux)  #agrego secuancialmente con append a aux en la lista sinrepetidos.

print("Lista original:", lista)
print("Lista sin repetidos:", sinrepetidos)
