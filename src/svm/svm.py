from sklearn import svm
import numpy as np
import cPickle as pickle
import features

class SVM:
	def __init__(self, C = 1.0, kernel = "rbf", gamma = 0.0, coef0 = 0.0, probability = True, tol = 0.001, verbose = False):
		self.clf = svm.SVC(C = C, kernel = kernel, gamma = gamma, coef0 = coef0, probability = probability, tol = tol)


	def train(self, features, targets):
		self.clf.fit(features, targets)


	'''
		Returns predicted class with probability.

		Format:
			(class, probability)
	'''
	def predict(self, feature):
		print (self.clf.predict(feature)[0], np.amax(self.clf.predict_proba(feature)) )


	'''
		Save SVM to file
	'''
	def save(self, name):
		try:
			pickle.dump(self.clf, open(name, "wb"))
		except:
			print "Could not save SVM"
			return False

		return True

	def load(self, name):
		try:
			self.clf = pickle.load(open(name, "rb"))
		except:
			print "Could not load SVM"
			return False
		return True