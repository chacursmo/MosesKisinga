#!/usr/local/bin/python3

###TODO Deal with Missing Values
#   The 200 year old problem

from math import log2

def main():


    a = buildtree()
#    printTree(a[0])

class Node(object):
    def __init__(self,data):
        self.data = data
        self.children = []

    def add_child(self,obj):
        self.children.append(obj)



def buildtree():
    root = []
    oldAttributes = []
    f = open("foo.csv","r")

    X = []
    T = []
    for l in f:
        l=l.strip()
        X.append(l.split(" "))

    f.close()

    f = open("moo","r")

    for l in f:
        l = l.strip()
        T.append(int(l))
    f.close()
    X2 = X
    T2 = T
    b = bestA(X2,T2,oldAttributes)
    oldAttributes.append(b)
    nN = Node(b)
    root.append(nN)
    currNode = nN
    print(nN.data)
    print("-----")
    #here
    A = getCol(X2,b)
    valsA = set(A)
    vAHos = list(valsA)
    for cidx in range(len(vAHos)):
        srt = []
        srt_T = []
        for mooidx in range(len(X2)):
            if int(X2[mooidx][nN.data]) == int(vAHos[cidx]):
                srt.append(X2[mooidx])
                srt_T.append(T2[mooidx])
        if len(srt) == 0:
            currNode.add_child(Node(1000))
        else :
            ayu = bestA(srt,srt_T,oldAttributes)
            oldAttributes.append(ayu)
            nNayu = Node(ayu)
            currNode.add_child(nNayu)

    for c in currNode.children:
        print (c.data, end=" ")
    print ("\n------")

    for c in currNode.children:
        A = getCol(X2,c.data)        
        valsA = set(A)
        vAHos = list(valsA)
        for cidx in range(len(vAHos)):
            srt = []
            srt_T = []
            for mooidx in range(len(X2)):
                if int(X2[mooidx][nN.data]) == int(vAHos[cidx]):
                    srt.append(X2[mooidx])
                    srt_T.append(T2[mooidx])
            if len(srt) == 0:
                c.add_child(Node(1000))
            else :
                ayu = bestA(srt,srt_T,oldAttributes)
                oldAttributes.append(ayu)
                nNayu = Node(ayu)
                c.add_child(nNayu)

    for curr in currNode.children:
        for c in curr.children:
            print (c.data,end=" ")
        print ("\n******")
    print("&&&")



    return root
    
    

    
def bestA(X,T,o):
    maxG = 0
    maxGidx = 0
    for idx in range(len(X[0])):
        if idx in o:
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
