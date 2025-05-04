class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
node1 = Node(2)
node2 = Node(4)
node3 = Node(6)
node4 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1 #to make it circular 

node4.prev = node3
node3.prev = node2
node2.prev = node1
node1.prev = node4 #to make it circular backwards


#traverse forward
currentNode = node1
while currentNode:
    print(currentNode.data, end = " ")
    currentNode = currentNode.next
    
print("")
#traverse backward
currentNode = node4
while currentNode:
    print(currentNode.data, end=" ")
    currentNode = currentNode.prev

# traverse through circular linkedlist
currentNode = node1
firstNode = node1
print(currentNode.data, end=" ") #printing the first node first
currentNode = currentNode.next   #then moving to the second node

while currentNode!=firstNode:       #from node2 if it goes in circle then stop at the node1
    print(currentNode.data, end=" ")
    currentNode = currentNode.next


    
