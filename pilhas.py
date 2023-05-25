dados = input().split()
mp = int(dados[0])
ma = int(dados[1])
val = str(input()).split()
v = []
for e in range(len(val)):
    v.append(int(val[e]))
while True:
    for e in range(len(v)):
        v[e] += 1
    print(v)
    
