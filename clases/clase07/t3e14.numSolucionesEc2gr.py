a: float = float(input("Valor de a: "))
b: float = float(input("Valor de b: "))
c: float = float(input("Valor de c: "))

resultado: str = ""
discriminante: float = b**2-4*a*c

if a==0 and b==0 and c==0:
    resultado = "Infinitas soluciones"
elif (a==0 and b==0 and c!=0) or (discriminante<0):
    resultado = "Tiene 0 soluciones reales"
elif (a==0 and b!=0) or (discriminante==0):
    resultado = "Tiene 1 solución real"
else:
    resultado = "Tiene 2 soluciones reales"
    
print(resultado)