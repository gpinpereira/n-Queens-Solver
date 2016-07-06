#Local Search


import sys as sys
import random as rd


def testSolution(sol):
    for k in range(len(sol)-1):
        for i in range(k+1,len(sol)):
            if(sol[k] == sol[i]+(i-k) or sol[k] == sol[i]-(i-k)):
                return False
    return True

def iterations(sol,n):

    for j in range(n):
        if(testSolution(sol)):
            rd.shuffle(sol)
        else:
            return j,sol
    return("No solution found in ",n," iterations")

n = int(sys.argv[1])
it = int(sys.argv[2])

st = range(n)

print(iterations(st,it))
