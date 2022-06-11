n = int(input())
if n in range(2, 4):
    print('На лугу пасется', n , "коровы")
else:
    temp = n % 10
    if temp in list(range(5, 10)) + [0]:
        print('На лугу пасется', n , "коров")
    if temp == 1:
        print('На лугу пасется', n , "коровa")
