import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg
import math
from operator import itemgetter
from pathlib import Path
import timeit

#general approch for least squares, works for any order polynomial approximation
#following functions are all untility function, nothing actually happens here
def coord_sum(coord, power):
	if(coord != 0 and coord != 1):
		print("Error")
		return 0
	sum = 0
	for point in data:
		x = point[coord]
		sum += x**power
	return sum

def yx_sum(power):
	sum = 0
	for point in data:
		x = point[0]
		y = point[1]
		sum += y*(x**power)
	return sum

def polynomial_approx(X, x):
	value = 0
	for degree in range(0, len(X)):
		value += X.item(degree,0)*x**degree
	return value

def find_coefficients(approximation_order):
	#sets up our A matrix
	matrix = []
	for row in range(0, approximation_order+1):
		row_matrix = [];
		for col in range(0, approximation_order+1):
			power = row+col
			row_matrix.append(coord_sum(0, power))
		matrix.append(row_matrix)
	A = np.matrix(matrix)
	#sets up our B matrix
	matrix = []
	for power in range(0, approximation_order+1):
		row_entry = [yx_sum(power)]
		matrix.append(row_entry)
	B = np.matrix(matrix)
	#solves our linear system
	X = linalg.solve(A,B)
	return X

def calcualte_R():
	den = len(data)*yx_sum(1)-coord_sum(0,1)*coord_sum(1,1)
	num = math.sqrt(len(data)*coord_sum(0,2)-coord_sum(0,1)**2)*math.sqrt(len(data)*coord_sum(1,2)-coord_sum(1,1)**2)
	return den/num

def calculate_Rsquared():
	y_average = coord_sum(1,1)/len(data)
	res = 0
	tot = 0
	for x in data:
		res += (x[1]-polynomial_approx(X, x[0]))**2
		tot += (x[1]-y_average)**2
	return 1-res/tot


def print_equation(X):
	equation = ""
	for num in range(0, len(X)):
		equation += str("x^"+str(num)+" coefficient => ["+ str(round(X.item(num,0), 4))+"]\n")
	#prints out our polynomial equation
	print("\nEquation:\n"+equation)
	if(len(X) == 2):
		print("\nR => "+str(calcualte_R()))
	else:
		print("R^2 =>"+str(calculate_Rsquared()))

def end():
	answer = str(input("would you like to try again? "))
	if(answer[0] == "y"):
		return False
	return True

#this is where the program actually starts, where we use all of the functions we have created
while True:
	#Reads in data from a text file, must be tab delimited
	fileName = str(input("Enter the name of the file with the data: "))
	while True:
		if(Path(fileName).is_file()):
			break
		else:
			fileName = str(input("File does not exist, please try again: "))
	data = np.loadtxt(fileName, 'float', delimiter="\t")
	#sets up some x coordinates so we can plot our trend line
	x_sample = np.arange(min(data, key=itemgetter(0))[0]-1, max(data, key=itemgetter(0))[0]+1, .01)
	approximation_order = (input("Enter the order of the requested polynomial fit: "))
	while True:
		try:
			int(approximation_order)
		except ValueError:
		    approximation_order = input("please enter a number: ")
		else:
			approximation_order = int(approximation_order)
			break
	starttime = timeit.timeit()
	X = find_coefficients(approximation_order)
	endtime = timeit.timeit()
	time  = endtime - starttime
	print("Run Time: " + str(time))
	print_equation(X)
	polynomial_x = x_sample
	polynomial_y = []
	#graphs the polynoial of best fit
	for x in polynomial_x:
		polynomial_y.append(polynomial_approx(X,x))
	#plots the original data points
	for point in data:
	 	plt.plot([point[0]], [point[1]], 'g^')
	plt.plot(polynomial_x, polynomial_y, 'r-')
	plt.ylim((min(data, key=itemgetter(1))[1]), (max(data, key=itemgetter(1))[1]))
	plt.show()
	if(end()):
		break
