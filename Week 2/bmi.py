#Calculates BMI
#takes input of weight in kilos and height in meters
from sympy import RealNumber

a = RealNumber(input('Enter your weight (KG)'))
b = RealNumber(input('Enter your height(M)'))

#9 & 10 Caluclate BMI as H/W squared
Newnumber = (a / b)
BMI = Newnumber**2   

#13 Prints the result
print('Your BMI is {}'.format(BMI))