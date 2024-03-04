
class Node:


    def __init__(self, move):
        self.Move = move
        self.R = None
        self.P = None
        self.S = None
        self.visited=False
        self.height= 0
        self.parent = None





def insertNode(root, newMove):
    if root == None:
        root = Node(newMove)
        root.parent = None
        return root

    if root.R is None and newMove == "R":
        if root.height>=5:
            return root
        root.R = Node(newMove)
        root.R.parent = root
        root.R.height=root.height+1
        return root

    if root.P is None and newMove == "P":
        if root.height>=5:
            return root
        root.P = Node(newMove)
        root.P.parent = root
        root.P.height=root.height+1
        return root

    if root.S is None and newMove == "S":
        if root.height>=5:
            return root
        root.S = Node(newMove)
        root.S.parent = root
        root.S.height=root.height+1
        return root

    insertNode(root.R,newMove)
    insertNode(root.P,newMove)
    insertNode(root.S,newMove)
    return root



    # if root.R is None:
    #     if root.height>5:
    #         return root
    #     root.R = Node(newMove)
    #     root.R.parent = root
    #     root.R.height=root.height+1
    # else:
    #     insertNode(root.R, newMove)
    # # print(newMove)
    # return root
    #
    # if root.P is  None:
    #     if root.height>5:
    #         return root
    #     root.P = Node(newMove)
    #     root.P.parent = root
    #     root.P.height = root.height + 1
    # else:
    #     insertNode(root.P, newMove)
    # # print(newMove)
    # return root
    #
    # if root.S is  None:
    #     if root.height>5:
    #         return root
    #     root.S = Node(newMove)
    #     root.S.parent = root
    #     root.S.height = root.height + 1
    # else:
    #     insertNode(root.S, newMove)
    # # print(newMove)
    # return root
    # else:
    #     print("Unknown move")
###########################################################################################################################






def getPlaySequence(Node):
    outArray = [Node.Move]
    parent = Node.parent
    while parent.Move is not None:
        outArray.append(parent.Move)
        parent = parent.parent
    return outArray

def makeSearchTree(root):
    for i in range(81):
        insertNode(root, "R")
        insertNode(root, "P")
        insertNode(root, "S")



def iterativeBFS(root):
    if root is None:
        print("No root")
        return root
    else:
        q=[]
        root.visited=True
        q.append(root)
    step=0

    while len(q)>0:
        step+=1
        currNode=q.pop(0)

        if currNode.Move is not None and not currNode.visited:
            currNode.visited=True
            # global prevPlaySequence
            # prevPlaySequence= playSequence
            # global playSequence
            playSequence= getPlaySequence(currNode)
            return playSequence



        out = ""
        if currNode.R is not None:
            # currNode.R.visited=True
            parent=currNode.parent
            out += currNode.R.Move
            while parent is not None:
                out+=parent.Move
                parent=parent.parent
            # print("step " + str(step) + ": " + out)
            q.append(currNode.R)

        out = ""
        if currNode.P is not None:
            # currNode.P.visited = True
            parent = currNode.parent
            out += currNode.P.Move
            while parent is not None:
                out += parent.Move
                parent = parent.parent
            # print("step " + str(step) + ": " + out)
            q.append(currNode.P)

        out = ""
        if currNode.S is not None:
            currNode.S.visited = True
            parent = currNode.parent
            out += currNode.S.Move
            while parent is not None:
                out += parent.Move
                parent = parent.parent
            # print("step " + str(step) + ": " + out)
            q.append(currNode.S)



# input=""
#





if input == "":

    Counter=0
    print(str(Counter)+" round")
    Counter +=1

    root=None
    root = insertNode(root, None)
    makeSearchTree(root)
    history = ["X", "X"]
    outputSequence = []
    print("round Start")
    Seq_exec_flag = False
    correctFlag = False
    # correctSequenceCounter=0
    correctSequence = []
    prevPlaySequence = []
    playSequence = []
    treeHeight=0
    output="R"


else:
    print(str(Counter) + " round")
    Counter += 1
    if len(history) > 0:
        history.pop(0)
        history.append(input)
    else:
        print(history)

    if history[0] == history[1] and not correctFlag:
        correctFlag = True
        correctSequence = prevPlaySequence.copy()
        playSequence = prevPlaySequence
        print("Wrong")


    if correctFlag and len(playSequence) > 0:
        output = playSequence.pop(0)
        print("Wrong2")

    elif correctFlag and len(playSequence) == 0:
        print("Wrong3")
        if history[0] == history[1]:
            playSequence = correctSequence
        else:
            correctFlag = False

    elif Seq_exec_flag == False:
        outputSequence = iterativeBFS(root).copy()
        print("sequence"+str(outputSequence))
        prevPlaySequence = outputSequence.copy()
        Seq_exec_flag = True
        output=outputSequence.pop(0)
    else:
        if len(outputSequence) > 1:
            print("stuck")
            output = outputSequence.pop(0)
        elif len(outputSequence) == 1:
            print("finished sequence")
            Seq_exec_flag = False
            output = outputSequence.pop(0)
        else:
            output = "R"
            print("something wrong happened")
            Seq_exec_flag = False
    print("2")











