import math
INF = math.inf

def findBestSuc():
    pass

def findWorstSucc():
    pass

def minimax(pos, dep, player):
    if dep == 0:
        staticVal = staticEvalute(pos)
        return [staticVal,[]]
    
    successors = gen(pos)
    if successors == []:
        staticVal = staticEvalute(pos)
        return [staticVal,[]]

    if player > 0:
        bestScore = -INF
        bestPath = None                
        for succ in successors:       
            opPos = minimax(succ,dep-1,-1*player)
            if opPos[0] > bestScore :
                bestScore = opPos[0]
                bestPath = opPos[2].insert(0,succ)
                
    else:
        bestScore = INF
        for succ in successors:
            pass

        
    
        
        