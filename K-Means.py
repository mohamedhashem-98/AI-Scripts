from sklearn.datasets import load_iris
from math import sqrt
def K_Means(dataset , numOfIterations , kk):
    centroids = [dataset[0] , dataset[50] , dataset[20]]
    clusters_old = [0 for i in range(150)]
    clusters_new = [0 for i in range(150)]
    for i in range(0 , 100):
            print(i)
            for j in range(0 , len(dataset)):
                centeroide_one = 0
                centeroide_two = 0
                centeroide_three = 0
                for k in range(0 , 4):
                    centeroide_one += pow(centroids[0][k] - dataset[j][k] , 2)
                    centeroide_two += pow(centroids[1][k] - dataset[j][k] , 2)
                    centeroide_three += pow(centroids[2][k] - dataset[j][k] , 2)
                centeroide_one = sqrt(centeroide_one)
                centeroide_two = sqrt(centeroide_two)
                centeroide_three = sqrt(centeroide_three)
                mini = min(centeroide_one ,min( centeroide_two , centeroide_three))
                if mini == centeroide_one :
                    clusters_new[j] = 0
                elif mini == centeroide_two :
                    clusters_new[j] = 1  
                elif mini == centeroide_three :
                    clusters_new[j] = 2
            c0 = [0 , 0 , 0 ,0]
            c1 = [0 , 0 , 0 ,0]
            c2 = [0 , 0 , 0 ,0]
            for zz in range(0 , len(dataset)):
                if clusters_new[zz] == 0 :
                    for x in range(0 , 4):
                        c0[x] += dataset[zz][x]
                    for x in range(0 , 4):
                        c0[x] = float(c0[x]) / clusters_new.count(0)
                    print(clusters_new.count(0))
                if clusters_new[zz] == 1 :
                    for x in range(0 , 4):
                        c1[x] += dataset[zz][x]
                    for x in range(0 , 4):
                        c1[x] = float(c1[x]) / clusters_new.count(1)
                if clusters_new[zz] == 2 :
                    for x in range(0 , 4):
                        c2[x] += dataset[zz][x]
                    for x in range(0 , 4):
                        c2[x] = float(c2[x]) / clusters_new.count(2)
            centroids[0] = c0
            centroids[1] = c1
            centroids[2] = c2 
            clusters_old = clusters_new
    return clusters_old     
            
data = load_iris()
dataset = data['data']
print(K_Means(dataset , 100 , 3))
