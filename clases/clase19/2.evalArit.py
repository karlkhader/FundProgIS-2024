# 2.evalArit.py

def evalArit(s):
    sum = 0
    for x in s:
        if x >= '0' and x <= '9':
            sum += int(x)

    return sum

# la siguiente es más potente
# ya que permitiría números de
# más de un dígito
def evalArit2(s):
    l = s.split('+')
    sum = 0
    for x in l:
        sum += int(x)

    return sum

print(evalArit("8+9+1"))
print(evalArit("9+0"))
print()
print(evalArit2("8+9+1"))
print(evalArit2("9+0"))
