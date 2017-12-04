import cPickle
from sklearn import datasets

iris = datasets.load_iris()
X, y = iris.data, iris.target


# load it again
with open('iris_SVM_classifier.pkl', 'rb') as fid:
    clf = cPickle.load(fid)

print clf.predict([X[0]])