def fun():
    i = 0
    c = 0
    while i < 10:
        j = 0
        while j < 10:
            print(c, end=" ")
            c += 1
            j += 1
        print()
        i += 1


fun()
