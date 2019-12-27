from math import *
x = [1, 2, 4, 3, 5]
y = [1, 3, 3, 2, 5]

# y = m*x + b

mean_x = sum(x) / len(x)
mean_y = sum(y) / len(y)
bast = 0
makam = 0
for i in range(0 , len(x)):
    bast += ((x[i] - mean_x) * (y[i]-mean_y))
    makam += ((x[i] - mean_x)**2)

m = bast / makam
b = mean_y - m * mean_x
y_new = [0 for i in range(5)]
for i in range(len(x)):
    y_new[i] = m * x[i] + b

RMSE = 0
for i in range(len(x)):
    RMSE += (y[i] - y_new[i])**2
RMSE /= len(x)
RMSE = sqrt(RMSE)

print(RMSE)