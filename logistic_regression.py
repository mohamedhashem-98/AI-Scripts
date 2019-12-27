import numpy as np
import math
import matplotlib.pyplot as plt

def sigmoid(x):
    # Activation function used to map any real value between 0 and 1
    return 1 / (1 + math.exp(-x))

def fit(x, y):
    L = 0.3  # The learning Rate
    epochs = 10  # The number of iterations to perform gradient descent
    b = [0, 0, 0]

    for j in range(epochs):
        for i in range(len(x)):
            prediction = predict_prob(b,x[i])
            b[0] = b[0] + L * (y[i]-prediction) * prediction * (1-prediction) * 1
            b[1] += L * (y[i]-prediction) * prediction * (1-prediction) * x[i][0]
            b[2] += L * (y[i]-prediction) * prediction * (1-prediction) * x[i][1]
    return b

def predict_prob(theta, x):
    # Returns the probability after passing through sigmoid
    net = theta[0] + theta[1]*x[0] + theta[2]*x[1]
    return sigmoid(net)

def predict_classes(theta,x):
    if predict_prob(theta, x) >= 0.5:
        return 1
    else:
        return 0

x = []
y = []

with open ('marks.csv') as fr:
    for line in fr:
        mark = line.split(',')
        x.append([float(mark[0]), float(mark[1])])
        y.append(int(mark[2]))

############ Plotting ############################
# filter out the applicants that got admitted
not_admitted = np.array(x[0:5])
# filter out the applicants that din't get admission
admitted = np.array(x[5:])

# plots
plt.scatter(admitted[:, 0], admitted[:, 1], s=10, label='Admitted')
plt.scatter(not_admitted[:, 0], not_admitted[:, 1], s=10, label='Not Admitted')
plt.show()
############ Fitting Classifier  ##################
cooefficients = fit(x, y)
print(cooefficients)

#################### Accuracy #####################
correct = 0

for i in range(len(x)):
    y_hat = predict_classes(cooefficients, x[i])

    if y_hat == y[i]:
        correct += 1

print (correct/len(x)*100)