for n in range(200, 1, -1):
    b = bin(n)[2:]
    if n % 2 == 0:
        b += '00'
    else:
        b += '11'
    r = int(b, 2)
    if r < 102:
        print(n)
        break
