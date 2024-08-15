

from email import message

k = 0
k = int(input('Enter Kelvin temperature measurement: '))
if k >= 0:
    print('{}°K is the K-scale temperature you have entered.'. format(k))
elif k < 0:
    print('Syntax Error, Kelvin is forbidden to enter less than 0.') 
    exit()

temp_str = input('Would you like to convert to [F/C]?')
temp = temp_str.lower() in ('f', 'c', 'fahrenheit', 'celsius')

f = (k - 273.15) * 9 / 5 + 32
c = k - 273.15

message = f"Here is your temperature calculated: "

if temp_str.lower() == 'f':
    message += ('{}°F.'. format(f))
elif temp_str.lower() == 'c':
    message += ('{}°C.'. format(c))

print(message)

print()
input('Press Enter to continue...')






