import math

print("\n============================================================================")
print("Q2. Modify the above script to contain a function (fruitful) to return the distance and call the same")
print("Same Programe with using function name as calc")
print("============================================================================\n")

x1=float(input('Please enter x1\t:'))
y1=float(input('Please enter y1\t:'))
x2=float(input('Please enter x2\t:'))
y2=float(input('Please enter y2\t:'))
def calc(x1,y1,x2,y2):
     d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
     return d    
print ("Distance\t:{:.2f}".format(calc(x1,y1,x2,y2)))
