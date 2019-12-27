import math
import matplotlib.pyplot as plt
from random import randint

class K_Means :
    def __init__(self , Matrix_of_data , Number_of_K , array_of_Labeld_data , Number_of_cols):
        self.Label_data = array_of_Labeld_data
        self.matrix_oper = [[0 for j in range(0 , Number_of_K + 1)]for i in range(0 , len(array_of_Labeld_data))]
        self.K = Number_of_K
        self.groups = [0 for i in range(0 , len(array_of_Labeld_data))]
        self.Data = Matrix_of_data
        self.cols = Number_of_cols
        self.cluters = [0 for i in range(0 , Number_of_K)]
        for i in range(0 , Number_of_K):
            List = []
            for j in range(0 , Number_of_cols):
                List.append(Matrix_of_data[i][j])
            self.cluters[i] = List

    def Train_data(self):
        while True :

            for i in range(0 , len(self.Label_data)):
                for j in range(0 , self.K):
                    var = 0.0
                    for k in range(0 , self.cols):
                        var += ((self.Data[i][k] - self.cluters[j][k])**2)
                        var = math.sqrt(var)
                    self.matrix_oper[i][j] = var

            for i in range(0 , len(self.Label_data)):
                Group_num = 1
                MIN = self.matrix_oper[i][0]
                for j in range(1 ,self.K):
                    if self.matrix_oper[i][j] < MIN:
                        MIN = self.matrix_oper[i][j]
                        Group_num = j+1
                self.matrix_oper[i][self.K] = Group_num
            check = True
            for i in range(0 , len(self.Label_data)):
                if self.matrix_oper[i][self.K] != self.groups[i]:
                    check = False
                    self.groups[i] = self.matrix_oper[i][self.K]
            if check == True:
                break
            Update = [[] for i in range(0 , len(self.cluters))]
            for i in range(0 , len(self.Label_data)):
                Update[self.groups[i]-1].append(self.Data[i])
            for i in range(0 , len(self.cluters)):
                Mean = [0.0 for indx in range(0 , len(self.cluters[i]))]
                for k in range(0 , len(Update[i])):
                    for x in range(0 , len(Update[i][k])):
                        Mean[x] += Update[i][k][x]
                for j in range(0 , len(Mean)):
                    Mean[j] = float(Mean[j]) / len(Update[i])
                self.cluters[i] = Mean

    def predict(self,Data):
        prediction = -1
        MIN = 999999999
        for i in range(0 , len(self.cluters)):
            Summation = 0.0
            for j in range(0 , len(self.cluters[i])):
                Summation+= ((Data[j] - self.cluters[i][j])**2)
            Summation = math.sqrt(Summation)
            if Summation < MIN:
                MIN = Summation
                prediction = i+1
        return prediction
    def Show_result_train(self):
        Res = [[]for i in range(0 , len(self.cluters))]
        for i in range(0 , len(self.groups)):
            Res[self.groups[i]-1].append(self.Label_data[i])
        for i in range(0 , len(self.cluters)):
            print("[" +str(i+1) + "] -> " + str(Res[i]))

    def plotting(self):
        colors = []
        for i in range(self.K):
            colors.append('#%06X' % randint(0, 0xFFFFFF))
        colorit = [0 for i in range(0 , len(self.Label_data))]
        for i in range(0 , len(self.Label_data)):
            colorit[i] = colors[self.groups[i]-1]
        x = [self.Data[i][0] for i in range(0 , len(self.Label_data))]
        y = [self.Data[i][1] for i in range(0, len(self.Label_data))]
        plt.scatter(x,y,c=colorit,s=150)
        plt.show()

# Example
# K must be less than Data
Matrix = [
    [2 , 10],
    [2 , 5],
    [8 , 4],
    [5 , 8],
    [7 , 5],
    [6 , 4],
    [1 , 2],
    [4 , 9]
]
k = 3
col = 2
Label = ['G1' ,'G2' ,'G3' ,'G4' ,'G5' ,'G6' ,'G7' ,'G8' ]
#x = [Matrix[i][0] for i in range(0 , 8)]
#y = [Matrix[i][1] for i in range(0 , 8)]
#plt.scatter(x,y)
#plt.show()
obj = K_Means(Matrix,k,Label,col)
obj.Train_data()
#obj.Show_result_train()
#print(obj.predict([2 , 1]))
obj.plotting()






