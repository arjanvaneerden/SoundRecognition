from sklearn import svm
import numpy as np
#from sklearn import preprocessing.MinMaxScaler as scale

class SVM:
	def __init__(self):
		print "Haha! Een SVM!"

	def getCochleagram(self):
		#FIXME read cochleagram files
		return

	def getAnnotation(self):
		#FIXME read annotation files
		return 
	
	def scaleData(self, data, (x, y)):
		scale = scale((x, y))
		return scale.fit_transform(data)


#	def optimize():


	def getFeatures(self, data):
		#FIXME multi channel support 
		#sum over column
		column = np.sum(data, 0)
		#sum over rows
		row = np.sum(data, 1)
		return (column, row)
