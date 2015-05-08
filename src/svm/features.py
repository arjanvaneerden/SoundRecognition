import numpy as np

class features:


	def getFeatures(self, array): 
		#sum over column
		column = np.sum(array, 0)
		#sum over rows
		row = np.sum(array, 1)

		return (column, row)

	def getCochleagram(self):
	#FIXME read cochleagram files
		return

	def getAnnotation(self):
		#FIXME read annotation files
		return 
	
	def scaleData(self, data, (x, y)):
		scale = scale((x, y))
		return scale.fit_transform(data)
