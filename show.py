valores = input().split()
pessoas = int(valores[0])
fileiras = int(valores[1])
fileira = list()
score  = 0
nfileira = fileiras
possiveis = [-1]
for i in range(fileiras):
    fileira = input().split()
    if '0' in fileira:
        starter = fileira.index('0')
        for e in range(starter, len(fileira)):
            if fileira[e] == '0':
                score += 1
            else:
                if score < pessoas:
                    score = 0
            if score >= pessoas:
                    possiveis.append(nfileira)
                    if -1 in possiveis:
                        possiveis.remove(-1)
        score = 0
    nfileira -= 1
print(min(possiveis))
    
