# a=0
# b=0
# c=0
# d=len(data)
# y_sum = 0;
# yx_sum = 0;

# for point in data:
# 	x = point[0]
# 	y = point[1]
# 	a += x**2
# 	b += x
# 	c += x
# 	y_sum += y
# 	yx_sum += y*x

# A = np.matrix([[a,b], [c,d]])
# print(inv(A))
# B = np.matrix([[yx_sum], [y_sum]])
# print("A matrix"+str(A))

# print("B matrix"+str(B))
# X = inv(A).dot(B)
# print(X)

# print("number of data points: "+str(len(data)))


# def linear_fit(m, b, x):
# 	return m*x+b
# plt.plot(x_sample, linear_fit(X.item(0,0), X.item(1,0), x_sample), 'b-')