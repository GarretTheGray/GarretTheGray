#!/bin/python3
import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*)(-_=+}][{\/?.><`'

length = input('Password length?')
length = int(length)

number = input('Number of passwords?')
number = int(number)

for p in range(number):

    password = ''
    for c in range(length):
        password += random.choice(chars)

    print(password)
