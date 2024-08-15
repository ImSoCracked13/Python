x = int(input("Enter 1st number:"))
y = int(input("Enter 2nd number:"))


if x % 2 == 0:
    result = "x is even and y is odd"
    print(result)
elif y % 2 == 0:
    result  = "x is odd and y is even"
    print(result)
elif x % 2 == 0 or y % 2 == 0:
    result = "both x and y are even"
    print(result)
else:
    result = "both x and y are odd"
    print(result)