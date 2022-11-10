n = int(input('pls input n: '))
if n >= 3 and n <= 9:
    for i in range(1, n + 1):
        for g in range(1, i + 1):
            print(g, end = "")
        for k in range(i - 1, 0, -1):
            print(k, end = "")
        print()
else:
    print('error numbeer')