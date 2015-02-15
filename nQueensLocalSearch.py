#Local Search


import sys as sys
import random as rd


def testSolution(sol):
    isSolution = True
    for k in range(len(sol)-1):
        if(not isSolution):
            break;
        for i in range(k+1,len(sol)):
            if(sol[k] == sol[i]+(i-k) or sol[k] == sol[i]-(i-k)):
                #print(i,sol[i])
                isSolution = False
                break
    if(isSolution):
        return 1,sol," is a solution!"
    else:
        return 0,sol," is not a solution!"

def iterations(sol,n):

    for j in range(n):
        #print testSolution(sol)
        if(testSolution(sol)[0]==0):
            rd.shuffle(sol)
        else:
            return j,sol
    return "No solution found in ",n," iterations"

n = int(sys.argv[1])
it = int(sys.argv[2])

st = range(n)

print iterations(st,it)
