import string
import random
length=int(input("enter the lenght:"))
a=[]
letter=string.ascii_lowercase
letter1=string.ascii_uppercase
digit=string.digits
special=("~``!@#$%^&*()_-+=<,./|'")
b=letter+letter1+digit
a.append(b)
f=random.sample(b,length)
password="".join(f)
password.replace(" ","")

print(password)
