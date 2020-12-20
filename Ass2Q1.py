"""Write a python script to solve the following.
A local shop sells three types of Laptops on Monday to Thursday- hp, sony and dell and the prices are 30000, 35000 and 40000 respectively. The sales of items are,
     Mon Tue wed Thu
hp   1    5   2   3
sony 5    6   3   1
dell 7    6   2   1
Using numpy, calculate the sales collection for each day."""


import numpy as np

total_s=[1,5,2,3],[5,6,3,1],[7,6,2,1]

total_sales=np.array(total_s)
hp=total_sales[0]
sony=total_sales[1]
dell=total_sales[2]
hp_sum=hp*30000
dell_sum=dell*40000
sony_sum=sony*35000
total_coll=np.array([hp_sum,dell_sum,sony_sum])
total_coll_ar=(total_coll.sum())
print("=========================================")
print("      Total Sales collection computer")
print("=========================================")
print("\t   Mon\t  Tue\t  Wed\t  Thu")
print("HP\t", hp_sum)
print("Sony\t",sony_sum)
print("Dell\t",dell_sum)
print("=========================================")
print("Total Sales of computer: Rs.",total_coll_ar)
print("=========================================")