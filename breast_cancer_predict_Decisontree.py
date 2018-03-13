import pandas as pd
from sklearn import cross_validation,tree
import numpy as np
data = pd.read_csv('/home/aman-py/Desktop/Data Science/breast_cancer.csv')
data.replace('?',-9999,inplace=True)
y = data['Class']
x = data.drop(['Sample code number'],1)
X = x.drop(['Class'],1)
X_train,X_test,y_train,y_test = cross_validation.train_test_split(X,y,test_size=0.20)
clf = tree.DecisionTreeClassifier()
clf.fit(X_train,y_train)
clf.score(X_test,y_test)
print(clf.score(X_test,y_test))
print(clf.predict([[1,2,3,4,5,6,7,8,9]]))
