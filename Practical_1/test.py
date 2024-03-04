from collections import deque
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
    if newMove == "R":
        if root.R is None:
            if root.height>=5:
                return
            root.R = Node(newMove)
            root.R.parent = root
            root.R.height=root.height+1
        else:
            insertNode(root.R, newMove)
        return root.R
    elif newMove == "P":
        if root.P is  None:
            if root.height>=5:
                return
            root.P = Node(newMove)
            root.P.parent = root
            root.P.height = root.height + 1
        else:
            insertNode(root.P, newMove)
        return root.P
    elif newMove == "S":
        if root.S is  None:
            if root.height>=5:
                return
            root.S = Node(newMove)
            root.S.parent = root
            root.S.height = root.height + 1
        else:
            insertNode(root.S, newMove)
        return root.S
    else:
        print("Unknown move")
###########################################################################################################################






def getPlaySequence(Node):
    outArray = [Node.move]
    parent = Node.parent
    while parent is not None:
        outArray.append(parent.Move)
        parent = parent.parent
    return outArray


def iterativeBFS(root):
    if root is None:
        print("No root")
        return root
    else:
        q=deque()
        root.visited=True
        q.append(root)
    step=0

    while len(q)>0:
        step+=1
        currNode=q.popleft()

        if currNode != root:
            if not  currNode.visited :
                currNode.visited=True

                # global prevPlaySequence
                prevPlaySequence= playSequence
                # global playSequence
                playSequence= getPlaySequence(currNode)
                return playSequence



        out = ""
        if currNode.R != None:
            currNode.R.visited=True
            parent=currNode.parent
            out += currNode.R.Move
            while parent is not None:
                out+=parent.Move
                parent=parent.parent
            print("step " + str(step) + ": " + out)
            q.append(currNode.R)

        out = ""
        if currNode.P != None:
            currNode.P.visited = True
            parent = currNode.parent
            out += currNode.P.Move
            while parent is not None:
                out += parent.Move
                parent = parent.parent
            print("step " + str(step) + ": " + out)
            q.append(currNode.P)

        out = ""
        if currNode.S != None:
            currNode.S.visited = True
            parent = currNode.parent
            out += currNode.S.Move
            while parent is not None:
                out += parent.Move
                parent = parent.parent
            print("step " + str(step) + ": " + out)
            q.append(currNode.S)



# input=""
#





if input == "":
    root = None
    root = insertNode(root, None)
    history = ["X", "X"]
    outputSequence = []
    Seq_exec_flag = False
    correctFlag = False
    # correctSequenceCounter=0
    correctSequence = []
    insertNode(root, 'R')
    prevPlaySequence = []
    playSequence = []
    treeHeight=0


else:
    history.pop(0)
    history.append(input)

    if history.index(0) == history.index(-1) and not correctFlag:
        correctFlag = True
        correctSequence = prevPlaySequence
        playSequence = prevPlaySequence


    if correctFlag and len(playSequence) > 0:
        output = playSequence.pop(0)

    elif correctFlag and len(playSequence) == 0:
        if history.index(0) == history.index(-1):
            playSequence = correctSequence
        else:
            correctFlag = False

    else:

        if  not Seq_exec_flag:
            outputSequence = iterativeBFS(root)
            Seq_exec_flag = True
            output=outputSequence.pop(0)
        else:
            if len(outputSequence) > 1:
                output = outputSequence.pop(0)
            else:
                output = outputSequence.pop(0)
                Seq_exec_flag = False







# root= insertNode(None,"R")
# insertNode(root,"P")
# insertNode(root,"S")
# insertNode(root,"R")
# insertNode(root,"R")
# insertNode(root,"S")
# insertNode(root,"S")
# insertNode(root,"P")
# insertNode(root,"R")
# insertNode(root,"S")
# insertNode(root,"P")
# iterativeBFS(root)




