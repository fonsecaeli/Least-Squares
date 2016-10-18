import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import inv
from numpy import linalg


#data = [(0.0, 0.1), (1.0, 0.9), (2.0, 2.2), (3.0, 2.8), (4.0, 3.9), (5.0, 5.1)]  #linear data set
data= [(10,	115.6),(15,157.2),(20,189.2),(24,220.8),(30,253.8),(34,269.2),(40,284.8),(45,285.0),(48,277.4),(50,269.2),(58,244.2),(60,231.),(64,180.4)] #quadratic data set
#data= [(0,-250),(10,0),(20,50),(30,-100)]
#data=[(0,0), (10,102.6903), (20,105.4529), (30,81.21744), (40,55.6016), (50,35.6859)]


#plots the data
for point in data:
 	plt.plot([point[0]], [point[1]], 'g^')

#sets up some x coordinates so we can plot our trend line
x_sample = np.arange(data[0][0]-10, data[len(data)-1][0]+10, .5)


###################################
#general approch, works for any order polynomial approximation
#gives results in slightly different forms than the above code
#
approximation_order = int(input("Enter the oder of the requested polynomial approximation: "))

def x_sum(power):
	sum = 0
	for point in data:
		x = point[0]
		sum += x**power
	return sum

def yx_sum(power):
	sum = 0
	for point in data:
		x = point[0]
		y = point[1]
		sum += y*(x**power)
	return sum

matrix = []
for row in range(0, approximation_order+1):
	row_matrix = [];
	for col in range(0, approximation_order+1):
		power = row+col
		row_matrix.append(x_sum(power))
	matrix.append(row_matrix)

A = np.matrix(matrix)

matrix = []
for power in range(0, approximation_order+1):
	row_entry = [yx_sum(power)]
	matrix.append(row_entry)

print(matrix)
B = np.matrix(matrix)
print("A matrix"+str(A))
print("B matrix"+str(B))

X = linalg.solve(A,B)


print(X)

def polynomial_approx(X, x):
	value = 0
	for degree in range(0, len(X)):
		value += X.item(degree,0)*x**degree
	return value

polynomial_x = x_sample
polynomial_y = []

for x in polynomial_x:
	polynomial_y.append(polynomial_approx(X,x))
	
plt.plot(polynomial_x, polynomial_y, 'r-')
plt.show()


 