x = input('words: ')
a = x.split(" ")
if (len(a)== 2):
    s1 = a[0]
    s2 = a[1]
    s1 = s1[::-1]
    s2 = s2[::-1]
    print(s1.capitalize(), s2.capitalize())
else:
    (len(a)== 1)
    a1 = input('pls input two words: ')
    b = a1.split(" ")
    s1 = b[0]
    s2 = b[1]
    s1 = s1[::-1]
    s2 = s2[::-1]
    print(s1.capitalize(), s2.capitalize())
