# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

# Reading and Understanding the Data
dataset = pd.read_csv('advertising.csv')

# Data Cleaning
# Exploratory Data Analysis
'''
By EDA we founf out that **TV** is highly corelated to Sales
'''
#Model Building - performing Simple Linear Regression

X = dataset.iloc[:,:3]
y = dataset.iloc[:, -1]

#Splitting Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(X, y)

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))

