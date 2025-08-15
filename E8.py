#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo:

altura=float(input("ingrese su altura: "))
peso=float(input("ingrese su peso: "))
imc=altura/(peso**2)
print(f"su altura es {altura}, su peso es {peso} y su indice de masa croporal es {imc}")
