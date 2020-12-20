# -*- coding: utf-8 -*-
"""Ass3Q3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hnuOfvEGFR-zgfiSkoyXa2CdHJQNV3zK

# Using diabetes dataset in sklearn, prepare an ML model using Linear regression to predict the value of disease progression. Print Root Mean Square Error values for a test data after splitting the data into train and test set. Also print the co-efficients of the linear model. (hint: model.coef_)
"""

from sklearn.datasets import load_diabetes
dia=load_diabetes()
X=dia.data
Y=dia.target
dia.feature_names

X[0:2]

Y[0:2]

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2, random_state=5)
print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)

X.shape

Y.shape

from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(X_train,Y_train)
p=model.predict(X_test)

Y_test

from sklearn.metrics import *
mse=mean_squared_error(Y_test,p)
print("Mean Squared erro: ",mse)
print("Coefficent Below\n",model.coef_)