numeros = []

# Le agregamos 3 números
for i in range(3):
  numero = float(input("Introduce el número #{}: ".format(i + 1)))
  numeros.append(numero)

# Asumir que el mayor es el primero de la lista
mayor = numeros[0]
# Recorrer y comparar
for numero in numeros:
    if numero > mayor:
        mayor = numero
# Segundo  Cambioiooooooooooooooooooooooooooo
print("Mayor:", numero)