from sklearn import svm
from sklearn import datasets
clf = svm.SVC()
iris = datasets.load_iris()
X, y = iris.data, iris.target
clf.fit(X, y)

import cPickle
# save the classifier
with open('iris_SVM_classifier.pkl', 'wb') as fid:
    cPickle.dump(clf, fid)

# load it again
with open('iris_SVM_classifier.pkl', 'rb') as fid:
    clf = cPickle.load(fid)