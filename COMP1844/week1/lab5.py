import math as m

a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
d = b*b-4*a*c

if a == 0 or d < 0:
    print('Math Error')
else:
    x1 = (-b+m.sqrt(b*b-4*a*c))/(2*a)
    x2 = (-b-m.sqrt(b*b-4*a*c))/(2*a)
    print('x1 =', x1)
    print('x2 =', x2)