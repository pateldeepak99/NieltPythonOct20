import math

print("\n============================================================================")
print("Q1. Write a script to display the distance between two points in XY plane")
print("There is two point calculation of distance. Where formula of used is: \nDistance=Square Root of (X2-X1)^2+(Y2+Y1^2). \nIt is applied in this Program. Using of math module ")
print("============================================================================\n")

x1=float(input('Please enter x1\t:'))
y1=float(input('Please enter y1\t:'))
x2=float(input('Please enter x2\t:'))
y2=float(input('Please enter y2\t:'))

d=math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print ("Distance\t:%.2f\n" %d)
