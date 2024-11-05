def punto_corte_rectas(a1: float, b1: float, a2: float, b2: float) -> float:
    x: float = (b2-b1)/(a1-a2)
    y: float = a1*x+b1
    return x,y

a1: int = int(input('Introduzca la pendiente de la primera recta: '))
b1: int = int(input('Introduzca el término indep. de la primera recta: '))

a2: int = int(input('Introduzca la pendiente de la segunda recta: '))
b2: int = int(input('Introduzca el término indep. de la segunda recta: '))

if (a1==a2):
    print('Las rectas no se cortan')
else:
    x,y = punto_corte_rectas(a1,b1,a2,b2)
    print('El punto de corte será: (',x,',',y,')')