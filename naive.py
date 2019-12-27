def read_file(filename):
    with open(filename) as fr:
        lines = fr.readlines()
    dataset = []
    for i in range(1 , len(lines)):
        dataset.append(tuple(lines[i].split(',')))
    return dataset
dataset = read_file("Naive_data.csv")
def count_number_of_calsses(dataset):
    classes = set()
    for i in range(0 , len(dataset)):
        classes.add(dataset[i][2])
    return classes , len(classes)

classes , numOfclasses = count_number_of_calsses(read_file("Naive_data.csv"))

def count_class_probability(dataset , classes , numOfclasses):
    P_classes = dict()
    for i in classes:
        count = 0
        for j in range(len(dataset)):
            if i == dataset[j][2]:
                count+=1
        P_classes[i] = float(count) / len(dataset)
    return P_classes

def NaiveBayes(vector , dataset , classes_Prob ):
    ans = [classes_Prob["Stay-Home\n"] , classes_Prob["Go-out\n"]]
    for i in range(0 , len(vector)):
        stayhome = 0 
        goout = 0
        for j in range(0 , len(dataset)):
            if vector[i] == dataset[j][i] and dataset[j][2] == "Go-out\n" :
                goout += 1
            if vector[i] == dataset[j][i] and dataset[j][2] == "Stay-Home\n" :
                stayhome += 1
        stayhome = float(stayhome) / 5
        goout = float(goout) / 5
        if stayhome != 0 :
            ans[0] = ans[0] * stayhome
        if goout != 0 :
            ans[1] = ans[1] * goout
    return ans
vector = ['Sunny' , 'Working']
classes_Prob = count_class_probability(dataset , classes , numOfclasses)
print(NaiveBayes(vector , dataset , classes_Prob))    