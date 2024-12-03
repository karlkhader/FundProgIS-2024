from random import randint
# Funciones
# Genera una baraja con todas las cartas ordenadas
def generar_baraja() -> list:
    baraja: list = []
    PALOS: list = ["diamantes", "tréboles", "corazones", "picas"]
    for p in PALOS:
        for valor in range(1, 11):
            carta: dict = {"valor": valor, "palo": p}
            baraja.append(carta)
    return baraja

# Desordena la baraja
def barajar(b: list) -> list:
    #baraja_desordenada: list = b[:] solo si queremos hacer una copia
    # Repetir 2000 veces:
        # generar dos valores aleatorios (dos posiciones de la lista b)
        # intercambiar los valores
    for i in range(2000):
        pos1: int = randint(0, len(b)-1)
        pos2: int = randint(0, len(b)-1)
        b[pos1], b[pos2] = b[pos2], b[pos1]
    return b

# Cuenta cuánto suman las cartas de un mano
def sumar_cartas(m: list) -> int:
    suma: int = 0
    # Sumar los valores de todas las cartas de m
    for c in m:
        suma += c["valor"]
    return suma

# Muestra las cartas de una mano 
def mostrar_mano(mano: list) -> None:
    # Escribe la carta con formato: valor de palo (sin salto de línea)
    for c in mano:
        print(f"{c['valor']} de {c['palo']}", end="")
        print(" | ", end= "")
    

# Programa principal
baraja: list = generar_baraja()
baraja = barajar(baraja) # mezcla las cartas

mano_jugador: list = []
mano_ordenador: list = []

suma_jugador: int = 0
suma_ordenador: int = 0

# Parte del jugador
continuar: bool = True 
while suma_jugador < 21 and continuar:
# 1.- Dar carta al jugador -> coja la primera de la baraja y añádela en la mano del jugador y bórrela de la baraja (use del)
    carta: dict = baraja[0]
    mano_jugador.append(carta)
    del(baraja[0])
# 2.- Sumar cartas del jugador
    suma_jugador = sumar_cartas(mano_jugador)
# 3.- Mostrar todas las cartas y su suma
    print("Jugador: ", end="")
    mostrar_mano(mano_jugador)
    print("Suma:", suma_jugador)
# 4a.- Si la suma de las cartas > 21 -> Pierde el jugador
# 4b.- Si la suma es <= 21 -> Preguntar al jugador si quiere otra carta -> Si quiere seguir volver a 1
    if suma_jugador <= 21:
        respuesta: str = input("¿Quieres otra carta (s/n)? ")
        continuar = (respuesta.lower() == 's')
    print()
    
# Parte de la cpu
# Repita mientras que ni el ordenador ni el jugador hayan perdido (> 21) y mientras el ordenador tenga menos que el jugador
while suma_ordenador < 21 and suma_jugador <= 21 and suma_ordenador < suma_jugador:
# 1.- Dar carta al ordenador -> coja la primera de la baraja y añádela en la mano del ordenador y bórrela de la baraja (use del)
    carta: dict = baraja[0]
    mano_ordenador.append(carta)
    del(baraja[0])
# 2.- Sumar cartas del ordenador
    suma_ordenador = sumar_cartas(mano_ordenador)
# 3.- Mostrar todas las cartas y su suma
    print("CPU: ", end="")
    mostrar_mano(mano_ordenador)
    print("Suma:", suma_ordenador)

# Resultado final
# Si el ordenador se ha pasado -> gana el jugador
# Si no gana el ordenador
print()
if suma_ordenador > 21:
    print("Has ganado!")
elif suma_ordenador == suma_jugador:
    print("Has empatado!")
else:
    print("Has perdido!")