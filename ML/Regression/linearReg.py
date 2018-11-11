import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
boston=load_boston()

df_x=pd.DataFrame(boston.data,columns=boston.feature_names)
df_x=df_x['AGE']
df_y=pd.DataFrame(boston.target)
lr=linear_model.LinearRegression()

x_train,x_test,y_train,y_test=train_test_split(df_x,df_y,test_size=0.2,random_state=5)
x_train=pd.DataFrame(data=x_train)
x_test=pd.DataFrame(data=x_test)
#x_train = x_train.values.reshape(-1,1)
#x_test = x_test.values.reshape(-1,1)
lr.fit(x_train,y_train)

a=lr.predict(x_test)

print(lr.coef_,lr.score(x_test,y_test),lr.intercept_)