idades = [int(input()), int(input())]
valoringresso = 0
for i in range(2):
    if idades[i] < 18:
        valoringresso += 15
    elif idades[i] < 59:
        valoringresso += 30
    elif idades[i] >= 60:
        valoringresso += 20
print(valoringresso)
