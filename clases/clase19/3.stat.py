# 3.stat.py
import math

def stats(nomFich: str) -> (float, float, dict):
    
    f = open(nomFich)
    caracter: int = f.read(1)
    suma: int = 0
    suma_al_cuadrado: int = 0
    num_numeros: int = 0
    dicc = {}
    while caracter != "":
        if caracter > '0' and caracter < '9':
            suma += int(caracter)
            suma_al_cuadrado += int(caracter)*int(caracter)
            num_numeros += 1
            if int(caracter) in dicc:
                dicc[int(caracter)] += 1
            else:
                dicc[int(caracter)] = 1
        caracter = f.read(1)
    f.close()   
    media: float = suma/num_numeros
    desv_tipica: float = math.sqrt((suma_al_cuadrado-suma**2/num_numeros)/(num_numeros-1))
    
    return media, desv_tipica, dicc
            
    
print(stats('datos.txt'))


