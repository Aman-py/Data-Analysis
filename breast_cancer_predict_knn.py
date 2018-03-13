import pandas as pd
from sklearn import cross_validation,neighbors
import numpy as np
data = pd.read_csv('/home/aman-py/Desktop/Data Science/breast_cancer.csv')
data.replace('?',-9999,inplace=True)
y = data['Class']
x = data.drop(['Sample code number'],1)
X = x.drop(['Class'],1)
X_train,X_test,y_train,y_test = cross_validation.train_test_split(X,y,test_size=0.20)
knn = neighbors.KNeighborsClassifier()
knn.fit(X_train,y_train)
print(knn.score(X_test,y_test))
print(knn.predict([[5,1,1,1,2,1,3,1,1]]))
