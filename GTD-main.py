#Importing Libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
#Importing the purified dataset
dataset = pd.read_csv("/Users/kushankurghosh/Documents/ML IT- Files/Project/GTD_Purified.csv")
#Splitting Dependent and independent variables to apply the algorithm
y_df = dataset.iloc[:,3]
x_df = dataset.iloc[:,[0,1,2,4,5,6]]
#Splitting Training and Testing Dataset
xtrain,xtest,ytrain,ytest = train_test_split(x_df,y_df, test_size=0.1, random_state=600)
#Applying logistic regression algorithm
logReg =LogisticRegression()
logReg.fit(xtrain,ytrain)
ypred = logReg.predict(xtest)
accuracy_score(ytest,ypred)
