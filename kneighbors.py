
import os
import sys
import imp
import operator
import numpy as np
from numpy import *
import matplotlib.pyplot as plt

imp.reload(sys)
# sys.setdefaultencoding('utf-8')

def dataSet():
	data = np.array([[1.0, 1.1], [1.0, 1.0], [0.0, 0.0], [0, 0.1]])
	label = ['A', 'A', 'B', 'B']
	return data, label


def drawImage():
	testdata = [0.2, 0.2]
	data, label = dataSet()
	fig = plt.figure(figsize=(8, 6))
	ax = fig.add_subplot(111)
	indx = 0
	for point in data:
		if label[indx] == 'A':
			ax.scatter(point[0], point[1], c='blue',
				marker='o', linewidths=0, s=300)
			plt.annotate('('+ str(point[0]) +', '+ str(point[1]) +')',
				xy=(point[0], point[1]))
		else:
			ax.scatter(point[0], point[1], c='red',
				marker='^', linewidths=0, s=300)
			plt.annotate('('+ str(point[0]) +', '+ str(point[1]) +')',
				xy=(point[0], point[1]))
		
		ax.scatter(testdata[0], testdata[1], c='green',
			marker='^', linewidths=0, s=300)
		plt.annotate('('+ str(testdata[0]) +', '+ str(testdata[1]) +')',
			xy=(testdata[0], testdata[1]))
		indx += 1
	
	plt.show()

drawImage()
