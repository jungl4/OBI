primeirovalor = int(input())
segundovalor = int(input())
valorsoma = int(input())
possiveis = ['-1']
t = ''
for i in range(primeirovalor, segundovalor + 1):
    v = list(str(i))
    ints = []
    for e in v:
        ints.append(int(e))
    soma = sum(ints)
    if soma == valorsoma:
        possiveis.append(v)
print(t.join(possiveis[len(possiveis)-1]))
           