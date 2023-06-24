saloes, tuneis, formiga = [int(x) for x in input().split()]
profundidade = [int(x) for x in input().split()] 
deslizes = []
maxv = -2000
ações = 0
for _ in range(tuneis):
    deslizes += [[int(x) for x in input().split()]]
#pegando as vars

formiga -= 1
for _ in range(tuneis):
    tempmaxv = maxv
    for e in range(tuneis):
        i, j = deslizes[e]
        i -= 1
        j -= 1
        if i == formiga:
            if profundidade[i] > profundidade[j] and profundidade[j] > maxv:
                maxv = profundidade[j]
                tempformiga = j
        elif j == formiga:
            if  profundidade[j] > profundidade[i] and profundidade[i] > maxv:
                maxv = profundidade[i]  
                tempformiga = i
        if tempmaxv != maxv:
            ações += 1
            formiga = tempformiga
            maxv = tempmaxv
print(ações)
