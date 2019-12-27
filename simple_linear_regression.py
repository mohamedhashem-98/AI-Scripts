
x = [1, 2, 4, 3, 5]
y = [1, 3, 3, 2, 5]


mean_x = sum(x) / len(x)
mean_y = sum(y) / len(y)

num = 0
den = 0

for i in range(len(x)):
    num += (x[i]-mean_x) * (y[i]-mean_y)
    den += (x[i]-mean_x) ** 2

b1 = num/den
b0 = mean_y - b1*mean_x

print (b1, b0)

########## Plotting ###################

import matplotlib.pyplot as plt

point_xs = [min(x), max(x)]
point_ys = [b0+b1*min(x), b0+b1*max(x)]

plt.scatter(x, y)
plt.plot(point_xs, point_ys, color='red')
plt.show()

########## Error ##################

sum1 = 0

for i in range(len(x)):
    sum1 += (y[i] - (b0 + b1*x[i]))**2

import math
print (math.sqrt(sum1/len(x)))