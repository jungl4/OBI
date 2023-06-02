v1, v2 = [int(input()), int(input())]

sa = [int(x) for x in input().split()]
sb = [int(x) for x in input().split()]

for e in sb:
    if e in sa:
        p1 = sa.index(e)
        for i in range(p1+1):
            sa[i] = 'a'
        confirmacao = 'S'
    else:
        confirmacao = 'N'
print(confirmacao)    
    