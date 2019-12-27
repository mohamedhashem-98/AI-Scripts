import numpy as np
import pandas as pd


def separate_by_class(dataset):
    separated = dict()

    for i in dataset.iterrows():
        class_value = i[1][2]

        if (class_value not in separated):
            separated[class_value] = list()

        separated[class_value].append(i)

    classcount= []

    for i in separated:
        classcount.append(len(separated[class_value]))

    return separated,classcount

def times(data,attribute,value):
    count = 0
    for i in data:
        if(i[1][attribute] == value):
            count = count+1

    return count


def Naive(input,data):
    max = 0
    count = 0
    label =''
    for i in data:
        classproperty = classcount[count]/datacount
        we = times(data[i],"Weather",input["weather"])
        CP_we = we / classcount[count]

        ca = times(data[i], "Car", input["car"])
        CP_ca = ca / classcount[count]
        prop = classproperty * CP_we *CP_ca
        if(prop >= max):
            max = prop
            label = i
    count= count+1
    return label

data = pd.read_csv('Naive_data.csv')
datacount = len(data)
data,classcount = separate_by_class(data)


input = {"weather":'Sunny',
         "car":'Working'}
print(Naive(input,data))







