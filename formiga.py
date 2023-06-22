salões, tuneis, formiga = [int(x) for x in input().split()]

prof_salões = [int(x) for x in input().split()]
tuneis_possiveis = []

for i in range(salões):
    while i + 2 <= len(prof_salões):
        if prof_salões[i] > prof_salões[i + 1]:
            tuneis_possiveis.append([prof_salões[i], prof_salões[i + 1]])
        break
print(tuneis_possiveis)