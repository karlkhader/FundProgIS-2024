# Ejercicio que transforma la hora optimizado
hora24: int = int(input("Hora: "))

# Supongo una configuración y solamente la cambio si lo necesito
modo: str = "pm"
    
if hora24 < 12:
    modo = "am"
    
if hora24 > 12:
    hora24 = hora24-12
    
print("Son las", hora24, modo)