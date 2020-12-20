"""2. Write a python script to solve the following.
A group of people took a trip on a bus at Rs.3.00 per child and Rs.3.20 per adult for a total of Rs.118.40
They took the train back at Rs.3.50 per child and Rs.3.60 per adult for a total of Rs.135.20.
Using numpy, print the number of children and adults."""

import numpy as np

A=np.array([[3,3.20],[3.50,3.60]])
b=np.array([118.40,135.20])
ans=np.linalg.solve(A,b) #using inbuilt function of algebra problem in numpy
print("Total Children\t: ",int(round(ans[0])))
print("Total Adult\t: ",int(round(ans[1])))