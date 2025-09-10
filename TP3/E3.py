#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.



print("Ingrese dos números y se sumarán los comprendidos entre ellos (excluyendo los extremos).")

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

suma = 0

# Aseguramos que numero1 sea el menor
if numero1 > numero2:
    numero1, numero2 = numero2, numero1


for numero in range(numero1 + 1, numero2): #al primero se sumo 1 para que lo excluya, al segundo lo excluye por defecto.
 
    suma += numero                          

print("La suma de los números comprendidos entre", numero1, "y", numero2, "es:", suma)

