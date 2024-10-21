altura: int = int(input("Dime la altura: "))

espacios: int = altura - 1
asteriscos: int = 1
for l in range(altura):
    for e in range(espacios):
        print(".", end="")
    for a in range(asteriscos):
        print("*.", end="")
    print()
    espacios -= 1
    asteriscos +=  1
    
