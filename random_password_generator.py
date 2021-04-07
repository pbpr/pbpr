import random

count=int(input("Enter password_length:"))
a = "01234567789"
b = "abcdefghijklmnopqrstuvwxyz"
c = "ABCDEFGHUJKLMNOPQRSTUVWXYZ"
d = "!@#$%^&?"
e = str( a + b + c + d)
password="".join(random.sample(e,count))
print("NEW RANDOM PASSWORD:",password)
