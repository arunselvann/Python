import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score

df = pd.read_csv('C:/Users/arunatesan/Desktop/Python/titanic/train.csv')

columns_target = ['Survived']
columns_train = ['Age','Pclass','Sex','Fare']

X = df[columns_train]
Y = df[columns_target]

X['Age']=X['Age'].fillna(X["Age"].median())
d={'male':0,'female':1}
X['Sex']=X['Sex'].apply(lambda x:d[x])

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))

# evaluate each model in turn
results = []
names = []
for name, model in models:
    score = cross_val_score(estimator = model, X = X_train, y = Y_train, cv = 10)
    results.append(score)
    names.append(name)
    msg = "%s: %f (%f)" % (name, score.mean()*100, score.std()*100)#multiplying by 100 to show percentage


# Compare Algorithms
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()