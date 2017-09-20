#!/usr/local/bin/python3

from math import log2

def main():


    d = getTest()

    for line in d:
        for item in line:
            print(str(item)+" ",end="")
        print("")


#    v = d[0]
 #   d = d[1]
#    g = open("moo","w")
#    for l in v:
#        g.write(str(l))
#        g.write('\n')
#    g.close()
    
#    f = open("foo.csv","w")
 #   for l in d:
  #      for i in l:
   #         f.write(str(i))
    #        f.write(' ')
     #   f.write('\n')

#    f.close()

#    T = buildTree(d,v)


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
        entropy.append(getEntropy(A[i],val))

    print (entropy)
    
    #find min entropy

    #set value as root

    #make branches


    #for each branch divide examples

    #find new node



    return A

def getEntropy(a,val):

    sA = set(a)

    lsA = list(sA)
    olsA = [0 for x in range(len(lsA))]
    
    for i in range(len(lsA)):
        olsA[i] = a.count(lsA[i])

    e = 0.0
    for i in range(len(lsA)):
        temp = olsA[i]/len(a)
        e += (temp)*log2(.5)
        


    pplus = val.count(1)/len(val)
    pminus = val.count(0)/len(val)

    actualEntropy = (-(pplus*log2(pplus)) - (pminus*log2(pminus)))
#    print(actualEntropy,e)
    gain = actualEntropy - e
    return gain


def getTest():
    f = open("../data/test.csv","r")
    colsName = f.readline()
    data = []
    for l in f:
        l = l.strip()
        l = l.split('"')

        if len(l) == 3:
            l = l[0]+l[2]
        elif len(l) == 7:
            l = l[0]+l[6]
        l = l.split(",")


        l.pop(2) 

        
        if l[2] == 'male':
            l[2] = 0
        else :
            l[2] = 1
        l[0] = int(l[0])
        l[1] = int(l[1])
        if l[3] != '':
            l[3] = int(float(l[3]))
        else :
            l[3]=200 #oh this causes a bug later on
        l[4] = int(l[4])
        l[5] = int(l[5])
        l.pop(6)

        if l[6] == '':
            l[6]=10

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
        l.pop(0)
        data.append(l)

    return data
        

def getData():
    f = open("../data/train.csv","r")

    colsName = f.readline()
    cn = colsName
    cn = cn.strip()
    cn = cn.split(",")
    cn.pop(3)
    cn.pop(-2)
    cn.pop(0)
    cn.pop(0)
    cn.pop(-3)
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
        targetValues.append(int(l.pop(1)))
        
        if l[2] == 'male':
            l[2] = 0
        else :
            l[2] = 1
        l[0] = int(l[0])
        l[1] = int(l[1])
        if l[3] != '':
            
            l[3] = int(float(l[3]))
        else :
            l[3]=200 #oh this causes a bug later on
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
        l.pop(0)
        data.append(l)
        print (cn)
        print (l)

    return [targetValues,data]
        

if __name__ == "__main__":
    main()
