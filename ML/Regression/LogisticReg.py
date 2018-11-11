import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

ad_data=pd.read_csv('C:/Users/arunatesan/Desktop/Docs/Python-Data-Science-and-Machine-Learning-Bootcamp/Machine Learning Sections/Logistic-Regression/advertising.csv')

X = ad_data[['Daily Time Spent on Site', 'Age', 'Area Income','Daily Internet Usage', 'Male']]
y = ad_data['Clicked on Ad']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.33,random_state=42)

logmodel=LogisticRegression()
logmodel.fit(X_train,y_train)

predictions=logmodel.predict(X_test)
print(classification_report(y_test,predictions))