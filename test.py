
class Node:
    #class for nodes in the search tree
    def __init__(self, move):
        self.Move = move
        self.R = None
        self.P = None
        self.S = None
        self.visited=False
        self.height= 0
        self.parent = None





def insertNode(root, newMove):
#function to insert a new node into the search tree
    #check if there is a root node
    if root == None:
        root = Node(newMove)
        root.parent = None
        return root
    # try to add a R node if root.R is None
    # return root if successful
    if root.R is None and newMove == "R":
        if root.height>=5:
            return root
        root.R = Node(newMove)
        root.R.parent = root
        root.R.height=root.height+1
        return root

    # try to add a P node if root.P is None
    # return root if successful
    if root.P is None and newMove == "P":
        if root.height>=5:
            return root
        root.P = Node(newMove)
        root.P.parent = root
        root.P.height=root.height+1
        return root

    # try to add a S node if root.S is None
    # return root if successful
    if root.S is None and newMove == "S":
        if root.height>=5:
            return root
        root.S = Node(newMove)
        root.S.parent = root
        root.S.height=root.height+1
        return root

    #recursive call of insertnode for all the moves

    insertNode(root.R,newMove)
    insertNode(root.P,newMove)
    insertNode(root.S,newMove)
    return root




###########################################################################################################################






def getPlaySequence(Node):
# function to aquire the play sequence of a node which consists of parents of a node
    outArray = [Node.Move]
    parent = Node.parent
    while parent.Move is not None:
        outArray.append(parent.Move)
        parent = parent.parent
    return outArray

def makeSearchTree(root):
# function to initialy create the search tree
    for i in range(81):
        insertNode(root, "R")
        insertNode(root, "P")
        insertNode(root, "S")



def iterativeBFS(root):
# BFS search to aquire the next sequence to be played
    if root is None:        #check if root is None
        print("No root")
        return root
    else:
        q=[]        #initialize the queue
        root.visited = True
        q.append(root)


    while len(q)>0: #check if there is a node in the queue

        currNode=q.pop(0)       #get the currNode from the stack

        if currNode.Move is not None and not currNode.visited:  #check if currennt node is valid and not yet visited
            currNode.visited=True
            playSequence= getPlaySequence(currNode)
            return playSequence

        # append currNode's children to the queue

        if currNode.R is not None:
            # currNode.R.visited=True
            parent=currNode.parent
            # out += currNode.R.Move
            while parent is not None:
                # out+=parent.Move
                parent=parent.parent
            # print("step " + str(step) + ": " + out)
            q.append(currNode.R)


        if currNode.P is not None:
            # currNode.P.visited = True
            parent = currNode.parent
            # out += currNode.P.Move
            while parent is not None:
                # out += parent.Move
                parent = parent.parent
            # print("step " + str(step) + ": " + out)
            q.append(currNode.P)

        # out = ""
        if currNode.S is not None:
            # currNode.S.visited = True
            parent = currNode.parent
            # out += currNode.S.Move
            while parent is not None:
                # out += parent.Move
                parent = parent.parent
            # print("step " + str(step) + ": " + out)
            q.append(currNode.S)



# input=""
def getCorrectMove(Move):
    if Move == "R":
        return "P"
    elif Move == "P":
        return "S"
    elif Move == "S":
        return "R"





if input == "":
    #initialize all variables

    Counter=0
    print(" round "+ str(Counter))
    Counter +=1
    root = insertNode(None, None)
    makeSearchTree(root)
    history = ["X", "X"]
    outputSequence = []
    print("round Start")
    Seq_exec_flag = False
    correctFlag = False
    correctSequence = []
    prevPlaySequence = []
    playSequence = []
    treeHeight=0
    output="R"


else:
    print(" round "+ str(Counter) )
    Counter += 1
    if len(history) > 0:  #check if there is a valid history
        history.pop(0)
        print("input : "+input)
        history.append(input)
    else:
        print(history)

    if history[0] == history[1] and not correctFlag:        #check if previous input results in a correct move
        correctFlag = True
        correctSequence = prevPlaySequence.copy()
        playSequence = prevPlaySequence
        print("correct sequence"+str(correctSequence))


    if correctFlag and len(playSequence) > 0:       #play the correct sequence
        output = playSequence.pop(0)
        print("move : "+str(output))

    elif correctFlag and len(playSequence) == 0: #finnish playing correct sequence

        if history[0] == history[1]: #check if sequence that was played was correct

            playSequence = correctSequence.copy()
            print("counter move :"+ getCorrectMove(history[1]))
            output = getCorrectMove(history[1])
            print("replaying sequence")
        else:
            print("incorrect sequence")
            correctFlag = False

    elif Seq_exec_flag == False or len(outputSequence) == 0: # get the and start playing the next sequence in the search tree
        outputSequence = iterativeBFS(root).copy()
        print("sequence"+str(outputSequence))
        prevPlaySequence = outputSequence.copy()
        Seq_exec_flag = True   # flag to indicate that the sequence is being played
        output=outputSequence.pop(0)
    else:
        if len(outputSequence) > 1:  # pla the sequence
            output = outputSequence.pop(0)
            print(outputSequence)
        elif len(outputSequence) == 1:  # disalble the flag and get the last move
            print(outputSequence)
            Seq_exec_flag = False
            output = outputSequence.pop(0)
            print("finished sequence")
        else:
            output = "R"
            print("something wrong happened")
            Seq_exec_flag = False


print("output : " + output)









