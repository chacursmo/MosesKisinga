#!/usr/local/bin/python3

###TODO Deal with Missing Values
#   The 200 year old problem

import random
import copy

from math import log2

def main():
    
    D = getData("trainingInstances.csv","targets.txt")

    goon(D)
    
def justOnPort(D):
    X = D[0]
    T = D[1]
    lst = []
    th = 0
    tw = 0
    on = 0
    zr = 0
    for idx in range(len(X)):
        lst.append(X[idx][5])
        if X[idx][6] == 3:
            if T[idx] == 1:
                th+=1
        elif X[idx][6] == 2:
            if T[idx] == 1:
                tw+=1
        elif X[idx][6] == 1:
            if T[idx] == 1:
                on+=1
        elif X[idx][6] == 0:
            if T[idx] == 1:
                zr+=1

    nvq = list(set(lst))
    print (len(nvq))

    
def goon(D):
    C = list(zip(D[0],D[1]))
    random.shuffle(C)
    a,b = zip(*C)
    l = int(len(a)/3)
    validA=a[l:]
    trainA=a[:l]
    validB=b[l:]
    trainB=b[:l]

    R = ID3(D[0],D[1],[0,1,2,3,4,5,6],True)

    T = getData("testInstances.csv","dontdo")
    T = T[0]

    results(T,R)




    
    
def pruning(D,R,a):
    T3 = copy.deepcopy(R)
    if len(T3.children) == 0:
        return T3
    else :
        for c in T3.children:
            temp = c
            T3.children.remove(c)
            vhu = numbertest(D,T3)
            if vhu > a:
                pass
            else :
                T3.children.append(c)
            return pruning(D,c,a)


    
def numbertest(D,R):
    result = 0
    for idx in range(len(D[0])):
        if predict(D[0][idx],R) == D[1][idx]:
            result += 1

    return result/len(D[0])
    


    
    

    
def testing(D,R):
    result = 0
    for idx in range(len(D[0])):
        if predict(D[0][idx],R) == D[1][idx]:
            result += 1

    print (str(result/(len(D[0]))*100)+"%")
    




def results(T,R):
    for idx in range(len(T)):
        if predict(T[idx],R):
            print (1)
        else:
            print(0)
        

    
def traverse(n):
    if len(n.children) == 0:
        print(1)
#        printNode(n)
    else :
        for c in n.children:
            traverse(c)

def printNode(n):
    print ("--------")
    print("Label is:" +str(n.label))
    print("# of Children:" +str(len(n.children)))
    print("Attribute Value is:" +str(n.attribute))
    print("Test attribute value is:" +str(n.test_attribute_value))
    print("+++++++++")
    
def predict(x,n):
    if n.label != None:
        return n.label
    else :
        temp = x[n.attribute]
        nc = None
        for c in n.children:
            nc = c
            if temp == c.test_attribute_value:
                break

        a = predict(x,nc)

        return a

    



            
        
        


class Node(object):
    def __init__(self,label=None,attribute=None,tav=None):
        self.label = label
        self.children = []
        self.attribute = attribute
        self.test_attribute_value = tav
        
    def add_child(self,obj):
        self.children.append(obj)

    def set_test_attribute_value(self,tav):
        self.test_attribute_value = tav
        
    def set_label(self,label):
        self.label = label
        
    def set_attribute(self,attribute):
        self.attribute = attribute





def getData(ex,ta):
    f = open(ex,"r")
    X = []
    T = []
    for l in f:
        l=l.strip()
        l = l.split(" ")
        l = [ int(x) for x in l]
        X.append(l)
    f.close()
    if ta == "dontdo":
        return [X,None]
    f = open(ta,"r")
    for l in f:
        l = l.strip()
        T.append(int(l))
    f.close()
    return [X,T]


def ID3(examples, Target_attribute, Attributes,state):
    root = Node()
    state = True
    for idx in range(len(Target_attribute)):
        if state and Target_attribute[idx] == False:
            state = False
    if state:
        root.set_label(True)
        return root
    state = True
    for idx in range(len(Target_attribute)):
        if state and Target_attribute[idx] == True:
            state = False
    if state:
        root.set_label(False)
        return root
    if len(Attributes) == 0:
        numPos = 0
        for idx in range(len(Target_attribute)):
            if Target_attribute[idx] == 1:
                numPos+=1
        numNeg = len(Target_attribute)-numPos
        if numPos > numNeg:
            root.set_label(True)
            return root
        else:
            root.set_label(False)
            return root


    A = bestA(examples,Target_attribute,Attributes)
    if state:
        A = 1 #sneaky bit here
        state = False
    root.set_attribute(A)
    workCol = getCol(examples,A)
    possibleValues = list(set(workCol))
    for idx in range(len(possibleValues)):
        examples_vi = []
        T_a_vi = []
        for idx2 in range(len(examples)):
            if examples[idx2][A] == possibleValues[idx]:
                examples_vi.append(examples[idx2])
                T_a_vi.append(Target_attribute[idx2])
        if len(examples_vi) == 0:
            newNode = Node()
            newNode.set_test_attribute_value(possibleValues[idx])
            root.add_child(newNode)
            numPos = 0
            for idx in range(len(Target_attribute)):
                if Target_attribute[idx] == 1:
                    numPos+=1
            numNeg = len(Target_attribute)-numPos
            if numPos > numNeg:
                newNode.set_label(True)
            elif numNeg > numPos:
                newNode.set_label(False)
            else:
                raise ValueError("End of Program")
        else :
            newAttributes = Attributes[:]
            newAttributes.remove(A)
            onDown = ID3(examples_vi,T_a_vi,newAttributes,state)
            onDown.set_test_attribute_value(possibleValues[idx])
            root.add_child(onDown)

    return root
    


def treeTest(X):
    if len(X) == 0:
        return False
    return True

def Learn(X,T):
    usedAttrib = []
    root = []
    hiGainIdx = bestA(X,T,usedAttrib)
    usedAttrib.append(hiGainIdx)
    currN = Node(hiGainIdx)
    if len(root) == 0:
        root.append(currN)
    workCol = getCol(X,hiGainIdx)
    setWorkCol = set(workCol)
    setList = list(setWorkCol)
    for idx in range(len(setList)):
        divyUp = []
        divyUp_T = []
        for idx2 in range(len(X)):
            if int(X[idx2][currN.data]) == int(setList[idx]):
                divyUp.append(X[idx2])
                divyUp_T.append(T[idx2])
                if len(srt) == 0:
                    currNode.set_leaf_value(1) # not corect
                else :
                    ayu = bestA(srt,srt_T,oldAttributes)
                    oldAttributes.append(ayu)
                    nNayu = Node(ayu)
                    currNode.add_child(nNayu)

    for c in currNode.children:
        A = getCol(X2,c.data)        
        valsA = set(A)
        vAHos = list(valsA)
        foziz = []

        for cidx in range(len(vAHos)):
            srt = []
            srt_T = []
            for mooidx in range(len(X2)):
                if int(X2[mooidx][nN.data]) == int(vAHos[cidx]):
                    srt.append(X2[mooidx])
                    srt_T.append(T2[mooidx])
            if len(srt) == 0:
                c.set_leaf_value(1) #not correct
            else :
                ayu = bestA(srt,srt_T,oldAttributes)
                oldAttributes.append(ayu)
                nNayu = Node(ayu)
                c.add_child(nNayu)

                

    return root


def I(p):
    pass


def distance(p_a,p_b):
    return (I(p_b/p_a) + I(p_a/p_b))

def bestA(X,T,o):
    return bestAG(X,T,o)
    

def splitInfo(S,A):
    pass


    
def bestAG(X,T,o):
    if len(o) == 1:
        return o[0]
    maxG = 0
    maxGidx = 0
    for idx in range(len(X[0])):
        if idx not in o:
            pass
        else :
            a = getCol(X,idx)
            G = gain(a,T)
            if  (G > maxG):
                maxG = G
                maxGidx = idx
    return maxGidx
    
def getCol(x,i):
    result = []
    for l in x:
        result.append(int(l[i]))

    return result


    
def entropy(t):

    survived = 0
    died = 0
    for i in t:
        if i == 1:
            survived += 1
        else :
            died += 1
    lt = len(t)
    if lt == 0:
        return 0
    elif survived == 0:
        p_d = died/lt
        e = -p_d*log2(p_d)
        return e
    elif died == 0:
        p_s = survived/lt
        e = -p_s*log2(p_s)
        return e
    else :
        p_s = survived/lt
        p_d = died/lt
        e = -p_s*log2(p_s) - p_d*log2(p_d)
        return e
    
def gain(x,t):
    A = set(x)
    A_int = []
    for idx in range(len(A)):
        A_int.append(int(list(A)[idx]))
    V = [0 for x in range(len(A))]
    Asort = sorted(A_int)
    for idx in range(len(x)):
        cv = int(x[idx])
        wwalf = Asort.index(cv)
        V[wwalf]+=1
    g = 0
    for idx in range(len(V)):
        S_v_t = []
        for ij in range(len(x)):
            if int(x[ij]) == (idx+1):
                S_v_t.append(t[ij])
            e = entropy(S_v_t)
        g+=(V[idx]/len(x))*e
    return entropy(t)-g
            

def printTree(N):
    if N is None:
        print ("leaf")
    else :
        print (N.data)
        for c in N.children:
            printTree(c)


if __name__ == "__main__":
    main()
