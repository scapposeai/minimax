import random

class Node:
    nodeCount=0
    def __init__ (self):
        self.children=[]
        self.score=0
        self.id="root"        

def createTree(id, width, depth, score, maxScoreChange):
    newNode = Node()
    Node.nodeCount=Node.nodeCount+1
    newNode.score = random.randint(score-maxScoreChange, score+maxScoreChange)
    newNode.id=id
    if depth==0:
        return newNode;
    
    for w in range(0,width):
        childNode = createTree(newNode.id + "-" + str(w), width, depth-1, newNode.score, maxScoreChange)
        newNode.children.append(childNode)
    return newNode

def printTree(node,indent):
    print("{}node[{}]:{}".format(indent, node.id, node.score))
    indent = indent + "    "
    for child in node.children:
        printTree(child, indent)
        
def negamax(tree, maxDepth, currentDepth):
    Node.nodeCount=Node.nodeCount+1
    #print("calling negamax({},{},{})".format(tree.id, maxDepth, currentDepth))
    if len(tree.children)==0 or currentDepth==maxDepth:
        #print("negamax for {} returns[{}]:{}".format(tree.id, tree.score, None))
        return tree.score, None

    bestMove = None
    bestScore=1000000

    for child in tree.children:
        recursedScore, currentMove = negamax(child, maxDepth, currentDepth+1)
        currentScore = recursedScore * (-1)
        if currentScore < bestScore:
            bestScore = currentScore
            bestMove = child
    #print("negamax for {} returns[{}]:{}".format(tree.id, bestMove.id, bestScore))
    tree.score=bestScore
    return bestScore, bestMove

def abNegamax(tree, maxDepth, currentDepth, alpha, beta):
    Node.nodeCount=Node.nodeCount+1
    #print("calling negamax({},{},{},{},{})".format(tree.id, maxDepth, currentDepth,alpha,beta))
    if len(tree.children)==0 or currentDepth==maxDepth:
        #print("negamax for {} returns[{}]:{}".format(tree.id, tree.score, None))
        return tree.score, None

    bestMove = None
    bestScore=1000000

    for child in tree.children:
        recursedScore, currentMove = abNegamax(child, maxDepth, currentDepth+1, beta*(-1), min(alpha, bestScore)*(-1))
        currentScore = recursedScore * (-1)
        if currentScore < bestScore:
            bestScore = currentScore
            bestMove = child

        if bestScore <= beta:
            return bestScore, bestMove
    #print("negamax for {} returns[{}]:{}".format(tree.id, bestMove.id, bestScore))
    #tree.score=bestScore
    return bestScore, bestMove

#Set widht and depth of tree
width=6
depth=6

#Create a tree, with width,depth, initial score, range of delta between child and parent score                           
myTree = createTree("t", width,depth,1000,50)
print ("NodeCount=" + str(myTree.nodeCount))

#Uncomment to print tree
#printTree(myTree,"")

#Run normal minimax function
Node.nodeCount=0
s, m = negamax(myTree,depth,0)
print ("negamax NodeCount=" + str(myTree.nodeCount))
print ("Best Move: " + m.id)
print ("Score: " + str(s))

#Run alphaBeta version
Node.nodeCount=0
s, m = abNegamax(myTree,depth,0,1000000,-1000000)
print ("abNegamax NodeCount=" + str(Node.nodeCount))
print ("Best Move: " + m.id)
print ("Score: " + str(s))

#Run alphaBeta version with narror window
Node.nodeCount=0
s, m = abNegamax(myTree,depth,0,1050,-1050)
print ("abNegamax NodeCount=" + str(Node.nodeCount))
print ("Best Move: " + m.id)
print ("Score: " + str(s))



