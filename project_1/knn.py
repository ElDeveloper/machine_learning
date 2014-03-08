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
from sklearn.neighbors import KNeighborsClassifier


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


results_distance = []
results_uniform = []
parameters = [(20, 'distance'),
              (20, 'uniform'),
              (30, 'distance'),
              (30, 'uniform'),
              (40, 'distance'),
              (40, 'uniform'),
              (50, 'distance'),
              (50, 'uniform'),
              (60, 'distance'),
              (60, 'uniform'),
              (70, 'distance'),
              (70, 'uniform')]


for element in parameters:
    print element
    if element[1] == 'distance':
        model = KNeighborsClassifier(n_neighbors=element[0], weights=element[1])
        model.fit(X_train_scaled, Y_train)
        results_distance.append(model.score(X_validation_scaled, Y_validation))

    else:
        model = KNeighborsClassifier(n_neighbors=element[0], weights=element[1])
        model.fit(X_train_scaled, Y_train)
        results_uniform.append(model.score(X_validation_scaled, Y_validation))


fd = open('knn_results.txt', 'w')
fd.write('Distance %s\n' % results_distance)
fd.write('Uniform %s\n' % resutls_uniform)
fd.close()

