#!/usr/local/bin/python3


def main():


    d = getData()


    v = d[0]
    d = d[1]


    T = buildTree(d,v)


def otherComment():
    test_data = getTestData()

    ids = test_data[0]
    test_data = test_data[1:]
    
    results = classifyTestData(T,test_data)
    printPredictions(results,ids)

def buildTree(dat,val):

    A = []

    for i in range(len(dat[0])):
        v = []
        for k in range(len(dat)):
            v.append(dat[k][i])
        A.append(v)
    
    entropy = []

    for i in range(len(A)):
        entropy.append(getEntropy(A[i]))

    
    #find min entropy

    #set value as root

    #make branches


    #for each branch divide examples

    #find new node



    return A

    

def getData():
    f = open("../data/train.csv","r")

    colsName = f.readline()

    data = []
    targetValues = []
    for l in f:
        l = l.strip()
        l = l.split('"')

        if len(l) == 3:
            l = l[0]+l[2]
        elif len(l) == 7:
            l = l[0]+l[6]

        l = l.split(",")

        l.pop(3) 

        targetValues.append(l.pop(1))
        
        if l[2] == 'male':
            l[2] = 0
        else :
            l[2] = 1
        l[0] = int(l[0])
        l[1] = int(l[1])
        if l[3] != '':
            
            l[3] = int(float(l[3]))
        else :
            l[3]=200
        l[4] = int(l[4])
        l[5] = int(l[5])
        l.pop(6) 
        l[6] = int(float(l[6]))
        l.pop(7)
        if l[7] == 'Q':
            l[7] = 0
        elif l[7] == 'C':
            l[7] = 1
        elif l[7] == 'S':
            l[7] = 2
        else:
            l[7] = 3
        data.append(l)

    return [targetValues,data]
        

if __name__ == "__main__":
    main()
