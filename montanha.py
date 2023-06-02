szseq = int(input())
seq = [int(x) for x in input().split()]
score = 0

for p1, p2, p3 in zip(seq, seq[1:], seq[2:]):
    if p1 > p2 < p3:
        print('S')
        break
    else:
        confirmacao = 'N'
if confirmacao == 'N':
    print(confirmacao)
