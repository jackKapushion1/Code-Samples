# This is a python function that takes in a set and retuns the power set.

def powerSet(A):
    pset = []
    for i in range(len(A)):
        pset.extend([[A[i]]])
        for j in range(len(pset)):
            if [A[i]] != pset[j]:
                add = []
                add.extend(pset[j])
                add.extend([A[i]])
                pset.extend([add])
    finalSet = [[]]
    finalSet.extend(pset)
    return finalSet


print(powerSet(['a','b','c','d']))

