v = input()
lista = [int(x) for x in input().split()]
score = 0

for e in range(len(lista)):
    k = -(e+1)
    if len(lista) > e:
        if lista[e] != lista[k]:
            sum1 = lista[e] + lista[e + 1]
                
            if sum1 != lista[k]:
                sum2 = lista[k] + lista[k - 1]
            
                if sum1 != sum2:
                    del lista[k], lista[-(e + 1)]
                    lista.insert(k, sum2)
                    
                else:
                    del lista[k], lista [k], lista[e], lista[e]
                    lista.insert(e, sum1)
                    lista.insert(e, sum1)
                    score += 1
            else:
                del lista[e], lista [e + 1]
                lista.insert(e, sum1)
                
            score += 1
   
print(score)
        