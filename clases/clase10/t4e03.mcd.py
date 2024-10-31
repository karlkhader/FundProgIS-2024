def MCD(a: int, b: int) -> int:
    mcd: int = a
    
    if a>b:
        mcd = b
        
    while a%mcd!=0 or b%mcd!=0:
        mcd -= 1
        
    return mcd


# Principal
# Apartado a)
print("El MCD de 20 y 6 es",MCD(20,6))

# Apartado b)
n1: int = int(input("Introduzca un número: "))
n2: int = int(input("Introduzca un número: "))
print("El MCD de",n1,"y",n2,"es",MCD(n1,n2))

# Apartado c)
print("El triple del MCD de",n1,"y",n2,"es",3*MCD(n1,n2))

# Apartado d)
print("El MCD de",n1+n2,"y",n1*n2,"es",MCD(n1+n2,n1*n2))

# Apartado e)
op1: float = n1*(n2/MCD(n1,n2))
op2: float = n2*(n1/MCD(n1,n2))
n1 = op1
n2 = op2
print(n1)
print(n2)

# Apartado f)
op1: int = MCD(n1,n2)
op2: int = MCD(n2,n1)
if op1==op2:
    print("El orden de los factores no altera el producto")
else:
    print("Debo revisar el código, nunca debí llegar aquí")