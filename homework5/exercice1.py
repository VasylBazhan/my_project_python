x = input('words: ')
a = x.split(" ")
if (len(a)== 2):
    s1 = a[0]
    s2 = a[1]
    s1 = s1[::-1]
    s2 = s2[::-1]
    print(s1.capitalize(), s2.capitalize())
else:
    print('pls input two words')


