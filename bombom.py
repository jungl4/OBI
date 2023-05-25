cartas = {'A': [10], 'J': [11], 'Q': [12], 'K': [13]}
dominante = input()[1]
Luana = list()
Edu = list()
tluana = tedu = 0

for i in range(3):
    Luana.append(input().split())
for i in range(3):
    Edu.append(input().split())

for i in Luana:
    if i[0][1] == dominante:
        tluana += 4 + cartas[f"{i[0][0]}"][0]
    else:
        tluana += cartas[f"{i[0][0]}"][0]
        
for i in Edu:
    if i[0][1] == dominante:
        tedu += 4 + cartas[f"{i[0][0]}"][0]
    else:
        tedu += cartas[f"{i[0][0]}"][0]

if tedu > tluana:
    print('Edu')
elif tedu < tluana:
    print('Luana')
else:
    print('empate')
