inicial, final = [int(x) for x in input().split()]

média = (inicial + final) / 2
valores = []
for i in range(inicial, final + 1):
    valores.append(i)
if (final - inicial + 1) // 2 != 0:
    e = 0
    while valores[e] != valores[-(e + 1)]:
        e += 1    
print(valores[e])
