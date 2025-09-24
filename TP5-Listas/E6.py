#6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
#último pasa a ser el primero).

lista = [1, 2, 3, 4, 5, 6, 7]
#Resueltp slicing
lista = lista[-1:] + lista[:-1] #toma el ultimo elemento (lista[-1:]) y se lo suma a todos los elementos menos el ultimo (lista[:-1])


print(lista)#Imprime la lista