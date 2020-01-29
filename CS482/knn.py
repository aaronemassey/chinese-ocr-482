import os
import numpy as np
from scipy import misc
from sklearn.neighbors import KNeighborsClassifier

training = 'training/'
testing = 'testing/'

NUMBEROFDIRS = len(os.listdir(training))


print "Loading data..."
train = [[np.array(misc.imread(training+set+'/'+image).flatten()) for image in os.listdir(training+set)] for set in os.listdir(training)]
train = np.concatenate(train, axis=0)

test = [[np.array(misc.imread(testing+set+'/'+image).flatten()) for image in os.listdir(testing+set)] for set in os.listdir(testing)]
test = np.concatenate(test, axis=0)

y = np.array([ a%NUMBEROFDIRS for a in range(len(train))])

print np.shape(train)
print np.shape(test)

neigh = KNeighborsClassifier(n_neighbors= NUMBEROFDIRS )

print "Training..."
neigh.fit(train, y)


print "Predicting..."
pred = neigh.predict(test)


print "Counting Errors..."
errors = np.count_nonzero(y - pred)

print "Number of errors =", errors
print "Total characters =", len(train)
print "Accuracy		    =",  1- float(errors) / float(len(train))
