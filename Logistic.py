import math
def read_dataset(filename):
    x = []
    y = []
    with open(filename) as fr:
        lines = fr.readlines()
    for i in range(len(lines)):
        tmp = lines[i].split(',')
        x.append([float(tmp[0]) , float(tmp[1])])
        y.append(int(tmp[2]))
    return x , y
def predict(b , x):
    val = b[0] + b[1] * x[0] + b[2] * x[1]
    prediction = 1 / (1 + math.exp(-val))
    return prediction
def Logistic(x,y):
    L = 0.3
    epochs = 10
    b = [0 , 0 , 0]
    for i in range(epochs):
        for j in range(len(x)):
            prediction = predict(b , x[j])
            b[0] = b[0] * L * (y[j] - prediction) * prediction * (1 - prediction) * 1
            b[1] += L * (y[j] - prediction) * prediction * (1 - prediction) * x[j][0]
            b[2] += L * (y[j] - prediction) * prediction * (1 - prediction) * x[j][1]           
    return b
def getclass(b , x):
    p = predict(b , x)
    if p >= 0.5:
        return 1 
    return 0
def accuracy(b , x , y):
    correct = 0
    for i in range(len(x)):
        y_label = getclass(b , x[i])
        
        if y_label == y[i]:
            correct += 1
    return (correct / len(x) ) * 100

x , y = read_dataset("marks.csv")
b = Logistic(x,y)
print(accuracy(b,x,y))