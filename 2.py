for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((x == y) or (y and z) or w) == 0:
                    print(x, y, z, w)
                    