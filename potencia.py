soma = 0

for i in range(int(input())):
    v = input()
    vp = int(v[-1])
    vn = int(v[:-1])
    soma += vn ** vp
print(soma)
