import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score

df = pd.read_csv('C:/Users/arunatesan/Desktop/Python/titanic/train.csv')
df1 = pd.read_csv('C:/Users/arunatesan/Desktop/Python/titanic/test.csv')
df.shape
df.Survived.value_counts()
df.Sex.value_counts().plot(kind='bar')

fig, axs = plt.subplots(1,2)
df[df.Sex == 'male'].Survived.value_counts().plot(kind='barh', ax = axs[0], title='Male')
df[df.Sex == 'female'].Survived.value_counts().plot(kind='barh', ax = axs[1], title='Female')

columns_target = ['Survived']
columns_train = ['Age','Pclass','Sex','Fare']

X = df[columns_train]
Y = df[columns_target]
X_test = df1[columns_train]
Y_test = df1[columns_target]
X['Age'].isnull().sum()
X['Pclass'].isnull().sum()
X['Sex'].isnull().sum()
X['Fare'].isnull().sum()
X_test['Age'].isnull().sum()
X_test['Pclass'].isnull().sum()
X_test['Sex'].isnull().sum()
X_test['Fare'].isnull().sum()

X['Age']=X['Age'].fillna(X["Age"].median())
X_test['Age']=X_test['Age'].fillna(X_test["Age"].median())
d={'male':0,'female':1}
X['Sex']=X['Sex'].apply(lambda x:d[x])
X_test['Sex']=X_test['Sex'].apply(lambda x:d[x])
X_test['Fare']=X_test['Fare'].fillna(X_test["Age"].mean())


clf = LinearSVC()
clf.fit(X, Y.values.flatten())

pred = clf.predict(X_test)

#cm = confusion_matrix(Y_test, pred)
score = cross_val_score(estimator = clf, X = X, y = Y.values.flatten(), cv = 10)
score.mean()
score.std()
clf.score(X,Y)
