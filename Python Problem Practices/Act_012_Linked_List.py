#my first attempt of creating linked list using my knowledge of C++ Linked list

class Node:     # creating a node
    def __init__(self, data):   # initialize attribute
        self.data = data        # for data
        self.next = None        # link of the next node

node1 = Node(12)                # initialize node and adding value
node2 = Node(31)
node3 = Node(12)

node1.next = node2              # assign the next node
node2.next = node3

currentNode = node1             # the first node will be the current in this initialization
while currentNode:
    print(currentNode.data)     # traversing every node
    currentNode = currentNode.next      #changing the current node to the next node
print("Null")
