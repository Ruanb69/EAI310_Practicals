bfs_dfs = 0
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
        if root.height >= 5:
            return root
        root.P = Node(newMove)
        root.P.parent = root
        root.P.height=root.height+1
        return root

    # try to add a S node if root.S is None
    # return root if successful
    if root.S is None and newMove == "S":
        if root.height >= 5:
            return root
        root.S = Node(newMove)
        root.S.parent = root
        root.S.height = root.height+1
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
# check if root is None
    if root is None:
        print("No root")
        return root
    else:
        # initialize the queue
        q=[]
        root.visited = True
        q.append(root)


    while len(q)>0: #check if there is a node in the queue
        # get the currNode from the stack
        currNode=q.pop(0)
        # check if currennt node is valid and not yet visited
        if currNode.Move is not None and not currNode.visited:
            currNode.visited=True
            playSequence= getPlaySequence(currNode)
            return playSequence

        # append currNode's children to the queue

        if currNode.R is not None:
            # currNode.R.visited=True
            # parent=currNode.parent
            # out += currNode.R.Move
            # while parent is not None:
                # out+=parent.Move
                # parent=parent.parent
#             print("step " + str(step) + ": " + out)
            q.append(currNode.R)


        if currNode.P is not None:
            # currNode.P.visited = True
            # parent = currNode.parent
            # # out += currNode.P.Move
            # while parent is not None:
            #     # out += parent.Move
            #     parent = parent.parent
#             print("step " + str(step) + ": " + out)
            q.append(currNode.P)

        # out = ""
        if currNode.S is not None:
            # currNode.S.visited = True
            # parent = currNode.parent
            # # out += currNode.S.Move
            # while parent is not None:
            #     # out += parent.Move
            #     parent = parent.parent
#             print("step " + str(step) + ": " + out)
            q.append(currNode.S)

def iterativeDFS(root):
    #check if root doesn't exist
    if root is None:
        print("No root")
        return root
    elif firstflag:  #initialize variables
        root.visited = True
        stack.append(root)

    while len(stack)>0: #while there are nodes in the stack, run this loop
        currNode = stack.pop()  #use node on the top of the stack

        if currNode.Move is not None and not currNode.visited:      #check if node is visited and doesn't have a move
            currNode.visited = True
            playSequence = getPlaySequence(currNode) #create the play sequence

            #add node children to the stack
            # append the R child to the stack
            if currNode.R is not None and not currNode.R.visited:
                stack.append(currNode.R)
            # append the P child to the stack
            if currNode.P is not None and not currNode.P.visited:
                stack.append(currNode.P)
            # append the S child to the stack
            if currNode.S is not None and not currNode.S.visited:
                stack.append(currNode.S)

            return playSequence

        #append the R child to the stack
        if currNode.R is not None and not currNode.R.visited:
            stack.append(currNode.R)
        # append the P child to the stack
        if currNode.P is not None and not currNode.P.visited:
            stack.append(currNode.P)
        # append the S child to the stack
        if currNode.S is not None and not currNode.S.visited:
            stack.append(currNode.S)

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
    firstflag=True
    stack=[]
    treeHeight=0
    if bfs_dfs ==0 :
        output="R"
    else:
        output="S"
    lastMoveinSequence = False


else:
    print(" round "+ str(Counter) )
    Counter += 1
    # check if there is a valid history
    if len(history) > 0:
        history.pop(0)
        print("input : "+input)
        history.append(input)
    else:
        print(history)
    # check if previous input results in a correct move
    if history[0] == history[1] and not correctFlag and lastMoveinSequence and len(prevPlaySequence)>1:
        correctFlag = True
        correctSequence = prevPlaySequence.copy()
        lastMoveinSequence = False
        #could be error
        playSequence = correctSequence.copy()
        print("correct sequence"+str(correctSequence))

    # play the correct sequence
    if correctFlag and len(playSequence) > 0:
        if history[0] != history[1] :
            if len(playSequence) == 1:
                lastMoveinSequence = True
            output = playSequence.pop(0)
            print("move : "+str(output))
        else:
            output = getCorrectMove(history[1])
            print("counter Move: "+output)

    # finnish playing correct sequence
    elif correctFlag and len(playSequence) == 0:

        # check if sequence that was played was correct
        if history[0] == history[1]:

            playSequence = correctSequence.copy()
            print("counter move :"+ getCorrectMove(history[1]))
            output = getCorrectMove(history[1])
            print("replaying sequence")
        elif lastMoveinSequence:
            print("incorrect sequence replying correct sequence")
            # print(correctSequence)
            # playSequence=correctSequence.copy()
            correctFlag = False
    # get the and start playing the next sequence in the search tree
    elif Seq_exec_flag == False or len(outputSequence) == 0:
        #Use the relevant search algotrithm
        if bfs_dfs == 0:
            outputSequence = iterativeBFS(root).copy()
        else:
            outputSequence = iterativeDFS(root).copy()
            firstflag=False
        lastMoveinSequence = False
        print("sequence"+str(outputSequence))
        prevPlaySequence = playSequence
        playSequence = outputSequence.copy()
        # flag to indicate that the sequence is being played
        Seq_exec_flag = True
        output=outputSequence.pop(0)

    else:
        # play the sequence
        if len(outputSequence) > 1:
            output = outputSequence.pop(0)
            print(outputSequence)

            # disalble the flag and get the last move
        elif len(outputSequence) == 1:
            print(outputSequence)
            lastMoveinSequence = True
            Seq_exec_flag = False
            output = outputSequence.pop(0)
            print("finished sequence")
        else:
            output = "R"
            print("something wrong happened")
            Seq_exec_flag = False


print("output : " + output)


##################################
#Single play results

# DFS

# total run time: 1.77 seconds
#
# breakable.py: won 0.0% of matches (0 of 10)
#     won 22.4% of rounds (2235 of 10000)
#     avg score -330.3, net score -3303.0
#
# eai320_prac_1_8.py: won 100.0% of matches (10 of 10)
#     won 55.4% of rounds (5538 of 10000)
#     avg score 330.3, net score 3303.0


#BFS

# total run time: 12.59 seconds
#
# breakable.py: won 0.0% of matches (0 of 10)
#     won 23.5% of rounds (2347 of 10000)
#     avg score -300.1, net score -3001.0
#
# test.py: won 100.0% of matches (10 of 10)
#     won 53.5% of rounds (5348 of 10000)
#     avg score 300.1, net score 3001.0

###############################################
# Multiple runs
# The following runs were obtained from running the prsrunner 5 time and averging the results

#BFS

#run time : 1.7 seconds
# round win rate : 48.78 %

#DFS

# run time : 1.674 seconds
# round win rate : 53.94 %


#########
#Discussion
# The win rate is affected mostly by what the break sequence is for each mach.
# The run time is affected by the different algorithm characteristics. Where BFS uses more searches to find the solution than DFS
# There were rare cases where the agent did not win all the matches this is most likely caused by certain sequences that are played that have not been accounted for
# in the agent logic.
