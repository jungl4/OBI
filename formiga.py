salões, tuneis, formiga = [int(x) for x in input().split()]

prof_salões = [int(x) for x in input().split()]
tuneis_possiveis = 0
            
for i in range(tuneis):
    p1, p2 = [int(x) -1 for x in input().split()]
    if prof_salões[p1] > prof_salões[p2] or prof_salões[p1] < prof_salões[p2] and formiga -1 == p1 or formiga -1 == p2:
        formiga = max(p1, p2)
        tuneis_possiveis += 1
print(tuneis_possiveis)
            
