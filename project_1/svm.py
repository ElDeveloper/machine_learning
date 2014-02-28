#!/usr/bin/env python
from __future__ import division

__author__ = "Yoshiki Vazquez Baeza"
__copyright__ = "Copyright 2013, Yoshiki Vazquez Baeza"
__credits__ = ["Yoshiki Vazquez Baeza"]
__license__ = "BSD"
__version__ = "unversioned"
__maintainer__ = "Yoshiki Vazquez Baeza"
__email__ = "yoshiki89@gmail.com"

from sys import argv

from numpy import genfromtxt, array

from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

C = float(argv[1])
gamma = float(argv[2])


# parse the CSV files
X_test = genfromtxt('forest_test.csv', delimiter=',')
train_data = genfromtxt('forest_train.csv', delimiter=',')
validation_data = genfromtxt('forest_validation.csv', delimiter=',')

print 'Test %s;Training %s; Validation %s' % (X_test.shape, train_data.shape, 
                                              validation_data.shape)

# separate the features from the labels
Y_train = train_data[:, -1]
X_train = train_data[:, :-1]

Y_validation = validation_data[:, -1]
X_validation = validation_data[:, :-1]

print 'X_train=%s,Y_train=%s; X_validation=%s,Y_validation=%s' % (
    X_train.shape, Y_train.shape, X_validation.shape, Y_validation.shape)


scaler = StandardScaler()
scaler.fit(X_train)

# scale the features
X_train_scaled = array(scaler.transform(X_train), dtype=float)
X_validation_scaled = array(scaler.transform(X_validation), dtype=float)

clf = SVC(C=C, cache_size=30000, class_weight=None, coef0=0.0, degree=3,
          gamma=gamma, kernel='rbf', max_iter=-1, probability=False,
          random_state=None, shrinking=True, tol=0.001, verbose=False)
clf.fit(X_train_scaled, Y_train) 

# score of the model
score = clf.score(X_validation_scaled, Y_validation)

fd = open('results.txt','a')
fd.write('The score is %f, C=%f, gamma=%f\n' % (score, C, gamma))
fd.close()

X_test_scaled = scaler.transform(X_test)
predictions = clf.predict(X_test_scaled)

# writting out the solutions file
fd = open('solutions_%f_%f.csv' % (C,gamma), 'w')
fd.write('Id,Prediction\n')
for index, prediction in enumerate(predictions):
    # add one to the index because identifieres in kaggle start at 1
    fd.write('%d,%d\n' % (index+1, prediction))
fd.close()


