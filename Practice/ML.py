import numpy as np
import pandas as pd
from numpy.random import randn
import matplotlib.pyplot as plt
import seaborn as sns
import plotly as pt
import cufflinks as cf
from scipy import linalg as la

a=np.array([[1,2,3],[4,5,6],[7,8,9]])

print(la.det(a))

x=np.linspace(0,5,11)
y=x**2
plt.plot(x,y)

fig,axes=plt.subplots(nrows=1,ncols=2)
for ax in axes:
    ax.plot(x,y,'b')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Title')

plt.show()