def encontrar_pos_valor(l:list, valor: float) -> int:
    posicion: int = -1
    ind: int = 0
    while ind < len(l) and posicion == -1:
        if l[ind] == valor:
            posicion = ind
        ind += 1
    return posicion

# --------------- PRINCIPAL ---------------
lista: list = [10, 6, 8, -5, 3, 2, 24, -12, 10, 1]

valor = 3
print('El valor', valor, 'está en la posición',encontrar_pos_valor(l,valor))