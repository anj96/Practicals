import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np


iris = datasets.load_iris()

print(iris.data)
iris_X = iris.data[:, np.newaxis, 0]
iris_Y= iris.data[:, np.newaxis,1]

print(iris_X)
print(iris_Y)

iris_X_train = iris_X[:-20]
iris_X_test = iris_X[-20:]

iris_y_train = iris.target[:-20]
iris_y_test = iris.target[-20:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(iris_X_train, iris_y_train)
