def mayor(l:list) -> float:
    mayor: float = l[0]
    for v in l:
        if v > mayor:
            mayor = v
    return mayor

# --------------- PRINCIPAL ---------------
lista: list = [10, 6, 8, -5, 3, 2, 24, -12, 10, 1]

print("El mayor de la lista es", mayor(lista))