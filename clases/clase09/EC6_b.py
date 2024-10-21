altura: int = int(input("Dime la altura: "))

# Primera línea
for a in range(altura*2-1):
    print("*", end="")
print()

# Calculo los espacios intermedios de la segunda línea
espacios2: int = 2*altura-5
#Recorro desde la segunda hasta la penúltima línea
for i in range(1,altura-1):
    # Imprimo los espacios iniciales en función de mi altura actual
    for s in range(i):
        print('.',end='')
    # Imprimo el primer asterisco
    print('*',end='')
    # Imprimo los espacios intermedios y el segundo asterisco después
    for s in range(espacios2):
        print('.',end='')
    print('*')
    # Reduzco los espacios intermedios para la siguiente iteración
    espacios2 -= 2

# Imprimo la última línea
for i in range(altura-1):
    print('.',end='')
print('*')