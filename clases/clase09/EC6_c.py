inferior: int = int(input("Parte de abajo: "))
superior: int = int(input("Dime la parte de arriba: "))

# Calculo la altura del trapezoide
altura: int = (inferior-superior)//2+1

# Imprimo la primera línea teniendo en cuenta la altura para los espacios
for s in range(altura-1):
    print('.',end='')
for i in range(superior):
    print('*',end='')
print()

# Calculo los espacios iniciales en función de la altura
espacios1: int = altura-2
# Calculo los espacios intermedios en función de la parte de arriba
espacios2: int = superior

# Recorro la parte intermedia de la figura
for i in range(1,altura-1):
    # Imprimo espacios iniciales y primer asterisco
    for s in range(espacios1):
        print('.',end='')
    print('*',end='')
    # Imprimo espacios intermedios y segundo asterisco
    for s in range(espacios2):
        print('.',end='')
    print('*')
    # Modifico los espacios para la siguiente línea
    espacios1 -= 1
    espacios2 += 2

# Imprimo la base inferior
for i in range(inferior):
    print('*',end='')