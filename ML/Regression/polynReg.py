import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

data=pd.read_csv('C:/Users/arunatesan/Desktop/Python/machinelearning/06 Polynomial Regression/Polynomial_Regression/Position_Salaries.csv')
X=data.iloc[:,1:2]
y=data.iloc[:,-1]

lr=LinearRegression()
lr.fit(X,y)

pr=PolynomialFeatures(degree=4)
X_poly=pr.fit_transform(X)

lr2=LinearRegression()
lr2.fit(X_poly,y)

# Visual LR
plt.scatter(X,y,color='red')
plt.plot(X,lr.predict(X),color='blue')
plt.title('Truth or Bluff(LR)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

#Visual PolyR
X_grid=np.arange(0,11,0.1)
X_grid=X_grid.reshape(len(X_grid),1)
plt.scatter(X,y,color='red')
plt.plot(X_grid,lr2.predict(pr.fit_transform(X_grid)),color='blue')
plt.title('Truth or Bluff(LR)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

#predict LR
print(lr.predict(6.5))

#Predict PloyR
print(lr2.predict(pr.fit_transform(6.5)))