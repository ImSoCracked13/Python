vowels = 'ueoai'
str = input('Enter a string: ')
print(str)
count = 0
for c in str:
    if c in vowels:
        count += 1
print(f'Number of vowels: {count}')



ac_name = input('Enter an Anime Character name: ')
print(ac_name)
if ac_name.isalpha():
    print('Valid name')
else:
    prind('Invalid name')



serial = input('Enter serial code: ')
print(serial)
if serial.isdigit():
    print('Valid serial code')
else:
    print('Invalid serial code')



name_tag = input('Enter your name tag: ')
print(name_tag)
position = name_tag.find('boss')
print(position)


print(name_tag.count('e'))
print(name_tag.endswith('com'))
print(name_tag.startswith('crosshair'))


