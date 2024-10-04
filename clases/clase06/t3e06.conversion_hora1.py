# Ejercicio que transforma la hora
hora24: int = int(input("Hora: "))

# Evito poner prints por todas partes, solo 1 y al final
if hora24 == 12:
    modo: str = "pm"
    
if hora24 < 12:
    modo: str = "am"
    
if hora24 > 12:
    hora24 = hora24-12
    modo: str = "pm"
    
print("Son las", hora24, modo)