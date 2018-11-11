import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import confusion_matrix

# Reading Data
dataset = pd.read_csv('C:/Users/arunatesan/Desktop/Python/machinelearning/31 Artificial Neural Networks/Artificial-Neural-Networks/Churn_Modelling.csv')

X = dataset.iloc[:,3:13].values
y = dataset.iloc[:,13].values

# Correcting Categorical Variables
labelencoder_X1 = LabelEncoder()
X[:, 1] = labelencoder_X1.fit_transform(X[:, 1])
labelencoder_X2 = LabelEncoder()
X[:, 2] = labelencoder_X2.fit_transform(X[:, 2])
onehotencoder = OneHotEncoder(categorical_features=[1])
X = onehotencoder.fit_transform(X).toarray()
X = X[:, 1:]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Feature Scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Initialising the ANN
classifier = Sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense(output_dim=6, kernel_initializer='uniform', activation='relu', input_dim=11))

# Adding the second hidden layer
classifier.add(Dense(output_dim=6, kernel_initializer='uniform', activation='relu'))

# Adding the output layer
classifier.add(Dense(output_dim=1, kernel_initializer='uniform', activation='sigmoid'))

# Compiling the ANN
classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Fitting the ANN to the Training set
classifier.fit(X_train, y_train, batch_size=10, nb_epoch = 100)

# Prediction
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
