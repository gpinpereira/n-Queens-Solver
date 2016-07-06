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
            return j,sol
        else:
            rd.shuffle(sol)
    return "No solution found in " + str(n) +" iterations"


it = int(sys.argv[2])
st = list(range(int(sys.argv[1])))

print iterations(st,it)
