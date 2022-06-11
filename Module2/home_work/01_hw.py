n = int(input())
m = int(input())
k = int(input())
s = m * n #Площадь шоколадки
if (k % n == 0 or k % m == 0 and k < s):
    print("YES")
else:
    print("NO")


