#Local Search



import random as rd
import itertools as it

pop5 = range(6)
pop4 = range(20)

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

def iterations(n,sol):

    for j in range(n):
        #print testSolution(sol)
        if(testSolution(sol)[0]==0):
            rd.shuffle(sol)
        else:
            return j,sol
    return "End of iterations"

print iterations(200,pop5)
print iterations(40000000,pop4)
