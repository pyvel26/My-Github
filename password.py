import random

chars = 'abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()~{}'

number = input('Number of passwords?')
number = int(number)
length = input ('Password length?')
length = int(length)
for p in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)