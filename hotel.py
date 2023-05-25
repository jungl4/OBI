valores = [int(input()), int(input()), int(input())]
if valores[2] == 1:
    x = 0
    
elif valores[2] > 1:
    x = valores[2] - 1
    if x > 14:
        x = 14
total = (32 - valores[2]) * (valores[0] + x * valores[1])
print(total)
