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


a = iterations(st,it)
ar=[0 for i in range(int(sys.argv[1]))]
str = ""


if isinstance(a, basestring ) == False: 
    a,b = iterations(st,it)
    print(b)    
    ar=b

for m in range(len(ar)):
    str = str + "__"    
str = str + "\n" 

#cria 1 linha de cada vez
for i,k in enumerate(ar):
#cria as parcelas de cada casa. Se a posicao dessa parcela for igual ao valor que esta no arra mete um Q senao e vazia 
    for j in range(len(ar)):        
        str = str + "|"
        # j+i para "sincronizar o tamanho do array com a posicao maxima a que a rainha pode estar"
        if j+1 == k: str = str + "Q"
        else: str = str + "_"
    str = str + "|"
    print(str)
    str = ""
