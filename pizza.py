v = [int(input()), int(input()), int(input()), int(input())]
r = ''
if v[0] * v[1] < 2 * 3.14 * v[2] or 360 % v[3] != 0:
    print('N')
else:
    print('S')
    