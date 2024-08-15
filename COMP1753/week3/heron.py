
a = int(input('Enter first Triangle side: '))
b = int(input('Enter second Triangle side: '))
c = int(input('Enter third Triangle side: '))
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c))**(1/2)
a + b > c 
b + c > a 
a + c > b 
if area > 0:
    print("{} is the Area of the Triagle calculated with Heron's Formula". format(area))
