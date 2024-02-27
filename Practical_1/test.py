from collections import deque
class Node:
    # R=None
    # P=None
    # S=None
    # Move=""
    # visited=None

    def __init__(self, move):
        self.Move = move
        self.R = None
        self.P = None
        self.S = None
        self.visited=False
        self.parent = None



class searchTree:
    def __init__(self):
        self.depth=5
        self.root=Node(None,None)

    def insertNode(self,root, newMove):
        if root == None:
            root = Node(newMove)
            root.parent = None
            return root
        if newMove == "R":
            if root.R == None:
                root.R = Node(newMove)
                root.R.parent = root
            else:
                self.insertNode(root.R, newMove)
            return root.R
        elif newMove == "P":
            if root.P is not None:
                root.P = Node(newMove)
                root.P.parent = root
            else:
                self.insertNode(root.P, newMove)
            return root.P
        elif newMove == "S":
            if root.S is not None:
                root.S = Node(newMove)
                root.S.parent = root
            else:
                self.insertNode(root.S, newMove)
            return root.S
        else:
            print("Unknown move")

    def iterativeBFS(self):
        root=self.root
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

            output = ""
            if currNode.R != None:
                currNode.R.visited=True
                parent=currNode.parent
                output += currNode.R.Move
                while parent is not None:
                    output+=parent.Move
                    parent=parent.parent
                print("step " + str(step) + ": " + output)
                q.append(currNode.R)

            output = ""
            if currNode.P != None:
                currNode.P.visited = True
                parent = currNode.parent
                output += currNode.P.Move
                while parent is not None:
                    output += parent.Move
                    parent = parent.parent
                print("step " + str(step) + ": " + output)
                q.append(currNode.P)

            output = ""
            if currNode.S != None:
                currNode.S.visited = True
                parent = currNode.parent
                output += currNode.S.Move
                while parent is not None:
                    output += parent.Move
                    parent = parent.parent
                print("step " + str(step) + ": " + output)
                q.append(currNode.S)



input=""
#
# if input == "":



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




