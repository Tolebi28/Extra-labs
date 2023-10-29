a = int(input())
b = int(input())
c = int(input())
if a >= b >= c:
    print(a, b, c)
elif a <= b <= c:
    print(c, b, a)
elif a >= b <= c:
    print(a, c, b)
elif b <= a <= c:
    print(c, a, b)
elif b >= a >= c:
    print(b, a, c)
elif b >= c >= a:
    print(b, c, a)