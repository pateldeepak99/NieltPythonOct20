print("\n============================================================================")
print("Q3. Write a script to check whether a given number is prime or not")
print("Enter positive number")
print("============================================================================\n")
x1 = int(input('Please enter Positive Number\t:'))
i = 2
while i <= x1/2:
    if(x1 % i == 0):
        #print(i)
        print("Number is NOT a prime")
        i=i+1
        break
    else:
        print("Number is a prime")
        break
else:
    if(x1!=2):
        print("Enter positive number or greater than 1 value allow")
    if(x1==2):
        print("Number is prime")  