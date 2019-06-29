#Importing Libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
#Importing the purified dataset
dataset = pd.read_csv("/Users/kushankurghosh/Documents/ML IT- Files/Project/GTD_Purified.csv")
#Encoding The column Provstate which contained text values
le = LabelEncoder()
x = dataset.iloc[:,2:3]
x = le.fit_transform(x)
#Encoding The column Gname which contained text values
y = dataset.iloc[:,9:10]
y = le.fit_transform(y)
#Replacing the columns Provstate and Gname with the encoded values of each type
dataset['provstate']=x
dataset['gname']=y
#Splitting Dependent and independent variables to apply the algorithm
y_df = dataset.iloc[:,10]
x_df = dataset.iloc[:,[6,7,5,11,12,13]]
#Splitting Training and Testing Dataset
xtrain,xtest,ytrain,ytest = train_test_split(x_df,y_df, test_size=0.05, random_state=600)
#Applying logistic regression algorithm
logReg =LogisticRegression()
logReg.fit(xtrain,ytrain)
ypred = logReg.predict(xtest)
accuracy_score(ytest,ypred)
