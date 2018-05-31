import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'

length = input('Password length? ')
length = int(length)
howmany = input('How many passwords do you want? ')
howmany = int(howmany)

for p in range(howmany):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)
