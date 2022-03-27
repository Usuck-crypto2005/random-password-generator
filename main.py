import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letter = "abcdefghijklmnopqrstuvwxyz"
digits = "1234567890"
symbols = "~`!@#$%^&*()_+-=|\;':'<>,./?{]}[ *"


# Just edit the true to false if you dont want any spesific category
upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letter
if nums:
    all += digits
if syms:
    all += symbols

length = 28
amount = 10  # change the amount to your choice

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)