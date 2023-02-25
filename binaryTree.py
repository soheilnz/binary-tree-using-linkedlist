# binary tree in which each node has at most 2 children.
# Types of binary tree :::
# {
#   1- full binary tree: each node has 0 or 2 children.
#   2- perfect binary tree: all node has 2 children and leaf nodes located in same level.
#   3- complete binary tree: all node has 2 children except last level.
#   4- balanced binary tree: all leaf nodes located in the same distance of root node.
# }

from queue_using_linkedlist import Queue

# from queue import Queue


# Creating binary tree using python list:
# {
#    first we start at index 1 for easier mathematical calculation.
#    LeftChild = cell[2x]   (( X ---> physical location of parent.))
#    RightChild = cell[2x + 1]
# }


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


newTree = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
newTree.leftChild = leftChild
newTree.rightChild = rightChild
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
cola = TreeNode("Cola")
fanta = TreeNode("Fanta")
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild.leftChild = cola
rightChild.rightChild = fanta

# ------------------------------------------------------------------------
# PreOrder Traversal:
# {Root Node ---> Left Subtree ---> Right Subtree.}


def PreOrder(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    PreOrder(rootNode.leftChild)
    PreOrder(rootNode.rightChild)


# PreOrder(newTree)

# ------------------------------------------------------------------------
# InOrder Traversal:
# {Left Subtree ---> Root node ---> Right subtree.}


def InOrder(rootNode):
    if not rootNode:
        return
    InOrder(rootNode.leftChild)
    print(rootNode.data)
    InOrder(rootNode.rightChild)


# InOrder(newTree)

# -------------------------------------------------------------------------
# PostOrder Traversal:
# {Left Subtree ---> Right Subtree ---> Root node.}


def PostOrder(rootNode):
    if not rootNode:
        return
    PostOrder(rootNode.leftChild)
    PostOrder(rootNode.rightChild)
    print(rootNode.data)


# PostOrder(newTree)

# -----------------------------------------------------------------------
# LevelOrder Traversal: ((FIFO method ---> first in first out.))
# { search level by level.}


def LevelOrder(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enQueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.deQueue()
            print(root.value.data)

            if root.value.leftChild is not None:
                customQueue.enQueue(root.value.leftChild)

                if root.value.rightChild is not None:
                    customQueue.enQueue(root.value.rightChild)


# LevelOrder(newTree)

# ---------------------------------------------------------------------------
#   for searching an element we use levelOrder traversal cause it uses queue but other traversal use stack memory.


def searchMethod(rootNode, nodeValue):
    if not rootNode:
        return "binary tree doesn't exist."
    else:
        customQ = Queue()
        customQ.enQueue(rootNode)
        while not customQ.isEmpty():
            root = customQ.deQueue()
            if root.value.data == nodeValue:
                return"Success"
            if root.value.leftChild is not None:
                customQ.enQueue(root.value.leftChild)

            if root.value.rightChild is not None:
                customQ.enQueue(root.value.rightChild)
        else:
            return "not found."


# LevelOrder(newTree)
# print(searchMethod(newTree, "Cola"))

# --------------------------------------------------------------------------------
#   for inserting a new node in a binary tree we use levelOrder traversal:
#   { first node in the lowest level that doesn't have 2 children we put new node in there.}


def insertNode(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQ = Queue()
        customQ.enQueue(rootNode)
        while not customQ.isEmpty():
            root = customQ.deQueue()
            if root.value.leftChild is not None:
                customQ.enQueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "success"

            if root.value.rightChild is not None:
                customQ.enQueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "success"


# newNode = TreeNode("with sugar")
# print(insertNode(newTree, newNode))
# newNode2 = TreeNode("No sugar")
# insertNode(newTree, newNode2)
# LevelOrder(newTree)

# ---------------------------------------------------------------------------
# Delete a node from binary tree:
#   { reach the deepest node(last node) in a binary tree using levelOrder traversal.then, we replace it with the node
#   that we want to delete.}


def getDeep(rootNode):
    if not rootNode:
        return
    else:
        customQ = Queue()
        customQ.enQueue(rootNode)
        while not customQ.isEmpty():
            root = customQ.deQueue()
            if root.value.leftChild is not None:
                customQ.enQueue(root.value.leftChild)

            if root.value.rightChild is not None:
                customQ.enQueue(root.value.rightChild)
        deepestNode = root.value
        return deepestNode


def deleteDeepNode(rootNode,deepNode):
    if not rootNode:
        return
    else:
        customQ = Queue()
        customQ.enQueue(rootNode)
        while not customQ.isEmpty():
            root = customQ.deQueue()
            if root.value is deepNode:
                root.value = None
                return
            if root.value.rightChild:
                if root.value.rightChild is deepNode:
                    root.value.rightChild = None
                    return
                else:
                    customQ.enQueue(root.value.rightChild)

            if root.value.leftChild:
                if root.value.leftChild is deepNode:
                    root.value.leftChild = None
                    return
                else:
                    customQ.enQueue(root.value.leftChild)


# newNode = getDeep(newTree)
# deleteDeepNode(newTree, newNode)
# LevelOrder(newTree)

def deleteNodeBT(rootNode, Node):
    if not rootNode:
        return "does not exist"
    else:
        customQ = Queue()
        customQ.enQueue(rootNode)
        while not customQ.isEmpty():
            root = customQ.deQueue()
            if root.value.data == Node:
                DNODE = getDeep(rootNode)
                root.value.data = DNODE
                deleteDeepNode(rootNode, DNODE)
                return " the node has been deleted."
            if root.value.leftChild is not None:
                customQ.enQueue(root.value.leftChild)

            if root.value.rightChild is not None:
                customQ.enQueue(root.value.rightChild)
        return "Failed."


# deleteNodeBT(newTree, "Tea")
# LevelOrder(newTree)

# -----------------------------------------------------------

#   Delete entire binary tree

def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None


deleteBT(newTree)
LevelOrder(newTree)
