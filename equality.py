#Tells if two numbers are equal
from sqlalchemy import false, true

x = int(input('enter a number'))
y = int(input('enter another number'))

if (x is y): 
    print(True)

if not(x is y):
    print(False) 