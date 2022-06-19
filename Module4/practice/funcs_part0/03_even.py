def even(n):
    if n % 2 == 0:
        return n
    print(False)
    pass

n = 7
if even(n):
    print('четное')
else:
    print('нечетное')
