
#TEST SHIT
from svm.svm import SVM
import random

if __name__ == "__main__":
	clf = SVM()

	features = []
	for i in range(0,100):
		features.append([random.random() - 0.5 for x in range(0,100)])

	teacher = [random.random() - 0.5 for x in range(0,100)]

	targets = []
	for feature in features:
		targets.append(sum([a * b for (a,b) in zip(feature, teacher)]))

	for i, target in enumerate(targets):
		if targets[i] <= 0:
			targets[i] = -1
		else:
			targets[i] = 1

	clf.train(features, targets)

	for feature in features:
		clf.predict(feature)

	clf.save("SVM.pkl")
	clf.load("SVM.pkl")

	