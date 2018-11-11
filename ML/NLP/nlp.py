import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
dataset = pd.read_csv('C:/Users/arunatesan/Desktop/Python/machinelearning/29 --------------------- Part 7 Natural Language Processing ---------------------/Natural_Language_Processing/Restaurant_Reviews.tsv',delimiter='\t',quoting=3)

# Cleaning The Texts
corpus = []
for i in range(0, len(dataset)):
    review = re.sub('[^a-zA-z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

# Creating the Bag of Words model
cv = CountVectorizer(max_features=1500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values

# Training the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state=0)
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Prediction
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
