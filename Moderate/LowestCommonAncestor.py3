import sys

class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val

def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.l_child == None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child == None:
                root.r_child = node
            else:
                binary_insert(root.r_child, node)

def linearLCA(root, node1, node2):
    if not root:
        return None

    if root == node1 or root == node2:
        return root
    else:
        left = linearLCA(root.l_child, node1, node2)
        right = linearLCA(root.r_child, node1, node2)

        if left and right:
            return root
        elif left:
            return left
        else:
            return right

path = sys.argv[1]
with open(path, 'r') as inFile:
    nodeList = list(map(Node, [30, 8, 52, 3, 20, 10, 29]))
    r = nodeList[0]
    binary_insert(r, nodeList[1])
    binary_insert(r, nodeList[2])
    binary_insert(r, nodeList[3])
    binary_insert(r, nodeList[4])
    binary_insert(r, nodeList[5])
    binary_insert(r, nodeList[6])

    for line in inFile:
        node1, node2 = map(int, line.rstrip().split())
        for node in nodeList:
            if node1 == node.data:
                node1 = node
                break
        for node in nodeList:
            if node2 == node.data:
                node2 = node
                break
        print(linearLCA(r, node1, node2).data)
