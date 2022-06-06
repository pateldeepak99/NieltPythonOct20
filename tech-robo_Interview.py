import math
''''
Def function use for example only we can also write simply in print function
E.g. in Addition choice, instead of calling sum function we can simplye write
  if(a==1):
        v1=int(input("Please Enter the First Value: "))
        v2=int(input("Please Enter the Second Value: "))
        print("Addition value:", v1+v2)
++++++++++++++++ Below is Tool and Python version information++++++++++++++++++++++
Python version = 3.8.6 (python --version)
Tools = VSCODE (latest)
User = Deepak Patel
Completed Time : 16-12-2020 (01:00 AM)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''

def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    return a/b
def mul2(a,b):
    return a*b
def pow(a,b):
    return a**b
def modulo(a,b):
    return a%b
flag=0
def ask():
    next=input("\n======================================================================\nPress any key to Continue, For exit, press 'N' ")
    if(next=='n' or next=='n'):
        return 1
    else:
        return 0
while flag==0:
    print('''\n======================================================================\nAssignment From Python Developer\nImplement Calucaltor in Python with blelow functionlity
1. Addition\n2. Substration\n3.Multiplicaton\n4.Division\n5.MOD\n6.X^Y\n7.Sin\n8.Cos\n9.Tan''')
    a=int(input("Please enter the Valid Choice:"))
    v1=0
    v2=0
    if(a>0 and a<7):
        v1=int(input("Please Enter the First Value: "))
        v2=int(input("Please Enter the Second Value: "))
    if(a>=7 and a<10):
        v1=int(input("Please enter the Value:"))
    if(a==1):
        print("Addition value:", sum(v1,v2)) #function used for exaple we can write simply print("Addition value:", v1+v2)
        flag=ask()
    elif(a==2):
        print("Substration Value:", sub(v1,v2))
        flag=ask()
    elif(a==3):
        print("Muliplication Answer:", mul2(v1,v2))
        flag=ask()
    elif(a==4):
        print("Division Value:", div(v1,v2))
        flag=ask()
    elif(a==5):
        print("Modulo Value:", modulo(v1,v2))
        flag=ask()
    elif(a==6):
        print("Power Value:", pow(v1,v2))
        flag=ask()
    elif(a==7):
        print(math.sin(v1))
        flag=ask()
    elif(a==8):
        print(math.cos(v1))
        flag=ask()
    elif(a==9):
        print(math.tan(v1))
        flag=ask()
    else:
        print("Exit the Program")
        flag=1