import sys



def possiblePlays(n):
    plays = []
    #Possible Plays
    for i in range(n):
        for j in range(n):
            plays.append((i,j))
    return plays

def firstMove(n):
    return [(0,i) for i in range(n)]

#computes forbidden "moves"
def cuts(pair):
    x,y = pair;
    cut = []
    for i in range(n):
        cut.append((x,i))
        cut.append((i,y))
    for i in range(n):

        if (y-i >= 0 and x+i < n):
            cut.append((x+i,y-i))
        if (x-i >= 0 and y+i < n):
            cut.append((x-i,y+i))
        if (y-i >= 0 and x-i >= 0):
            cut.append((x-i,y-i))
        if (y+i < n and x+i < n):
            cut.append((x+i,y+i))
    return list(set(cut))


#solveTheQueens:
    #Input: firstMove -> the first move
            #plays -> every possible position in the board
            #n -> n-Problem NEED TO ADDRESS THIS
            #prevForbMoves -> forbidden moves due to the queens on the table
            #level -> "Depth of the tree"
            #sol-> possible branch (contains all previous moves)
            #solutionSet -> default, to prevent early returns and to go down the tree
    #Outputs:
            #The solution set if level == n, a list of lists of tuples
            #Nothing

    #Inner Workings:
            #It will try to recursively find every solution by a depth first search until the end of the tree
            #-----not the most efficient method----
            #Starts by computing the forbidden locations, caused by the queens placed on the board.
            #If there aren't any allowed locations (i.e empty list of moves) it will break.
            #If there are allowed locations it will recursively until the current level is the same as the given n
            #If there's atleast one allowed location at n level, then a solution was found.
            #Each solution will be added to the solution set
def solveTheQueens(firstMove,plays,n,prevForbMoves = [],level=0,sol = [],solutionSet = []): #possible first moves,possible plays
    level +=1
    for i in firstMove:

        solution = [i]
        solution.extend(sol)

        currentForbMoves = cuts(i)   #non allowed plays currentForbMoves
        currentForbMoves.extend(prevForbMoves) #extending previous non allowed plays -Recursivity feature-

        nextMove = [k for k in plays if k not in currentForbMoves and k[0] == level]

        if nextMove:
            solveTheQueens(nextMove,plays,n,currentForbMoves,level,solution)
        elif level == n:
            solutionSet.append(solution)
        else:
            break
    return solutionSet


#Example


n = int(sys.argv[1])

plays = possiblePlays(n)
print solveTheQueens(firstMove(n),plays,n)
