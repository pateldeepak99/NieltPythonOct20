# -*- coding: utf-8 -*-
"""Ass3Q1&Q2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uqhcG2b2PZ8BlrphdyrZSMPEc6xJUH08

# 1. Prepare an ML model using KNN Classifier to predict the Species information for a given iris flower using Sepal Length, Sepal Width, Petal Length & Petal Width. 
Use the complete iris dataset for training. Use it to  predict the species of an iris flower.
"""

from sklearn.datasets import load_iris
iris=load_iris()
iris.feature_names

X=iris.data
y=iris.target

X.shape

y.shape

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(3)
knn.fit(X,y)

print(knn.predict(X[[120]]))

print(knn.predict(X))

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

knn2=KNeighborsClassifier(3)
knn2.fit(X_train,y_train)

knn2.predict(X_test)

print(y_test)

from sklearn.metrics import accuracy_score,confusion_matrix
print(knn2.predict(X_test))

"""# 2. Print the Accuracy Score and Confusion matrix for KNN Classifier using iris data.
# (Split iris dataset to train and test sets.)
"""

print(accuracy_score(y_test,knn2.predict(X_test)))

print(confusion_matrix(y_test,knn2.predict(X_test)))

"""# 3. Using diabetes dataset in sklearn, prepare an ML model using Linear regression to predict the value of disease progression. Print Root Mean Square Error values for a test data after splitting the data into train and test set. Also print the co-efficients of the linear model. (hint: model.coef_)"""

