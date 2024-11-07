def posicion_del_mayor(l:list) -> int:
    pos_mayor: int = 0
    for ind in range(1,len(l)):
        if l[ind] > l[pos_mayor]:
            pos_mayor = ind
    return pos_mayor

# --------------- PRINCIPAL ---------------
lista: list = [10, 6, 8, -5, 3, 2, 24, -12, 10, 1]

m = posicion_del_mayor(lista)
print("El menor de la lista es", lista[m], "y está en la posicion", m)