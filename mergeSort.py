# This is a recursive python code that takes a list of integers as input and returns a list of the integers from smallest to greatest.

def merge(L1, L2):
    L = []
    while len(L1) != 0 and len(L2) != 0:
        if L1[0] < L2[0]: 
            print(L1[0], '<', L2[0], sep="")
            L += [L1[0]] 
            L1.remove(L1[0])
            if len(L1) == 0:
                L += L2
                L2 = []
        if len(L1) != 0 and len(L2) != 0:
            if L2[0] < L1[0]:
                print(L2[0], '<', L1[0], sep="")
                L += [L2[0]]
                L2.remove(L2[0])
                if len(L2) == 0:
                    L += L1
                    L1 = []
    return L

def mergeSort(L):
    if len(L) > 1: 
        L1 = L[0 : (int(len(L)/2))] 
        L2 = L[(int(len(L)/2)) : len(L)]
        L = merge(mergeSort(L1), mergeSort(L2)) 
    return L

print(mergeSort([2,1,8,3]))
