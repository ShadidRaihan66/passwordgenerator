import random
import string

lenth = int(input('\nEnter the lenth of password: '))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
numb = string.digits
symbol = string.punctuation

all = lower + upper + numb + symbol

temp = random.sample(all, lenth)
password = "".join(temp)

print(password)