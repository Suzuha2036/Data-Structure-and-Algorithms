class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def searchAlgo(head):
    currentNode = head.next #moving to the second node
    minValue = head.data    #get the first node data as minValue 
    while currentNode:
        if currentNode.data < minValue: #compare the currentNode data (which is 2nd node) and minValue which is first node data
            minValue = currentNode.data #if true change the minValue data to currentnode data
        currentNode = currentNode.next  #move to the next node
    return minValue                     #after the traversal, return the minValue


node1 = Node(11)
node2 = Node(13)
node3 = Node(7)
node4 = Node(4)
node5 = Node(24)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("The lowest Value is", searchAlgo(node1))



    