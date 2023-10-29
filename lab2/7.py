a = int(input())
b = int(input())
c = int(input())
#ax2+bx+c=0
d = (b**2) - (4*a*c)
e = 2 * a

if d == 0:
    print(-b/(2*a))
elif d > 0:
    print((-b + (d**(1/2))) / e, (-b - (d**(1/2))) / e)