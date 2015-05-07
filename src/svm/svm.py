from sklearn import svm
import numpy as np
class SVM:
	def __init__(self):
		print "Haha! Een SVM!"

	def getFeatures(self, array): 
		#sum over column
		column = np.sum(array, 0)
		#sum over rows
		row = np.sum(array, 1)
		return (column, row)
