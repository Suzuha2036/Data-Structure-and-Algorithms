class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverse(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" ")
        currentNode = currentNode.next
    print("null")


def addNode(head, newNode, position):
    if position == 1:
        newNode.next = head
        return newNode
        
    currentNode = head
    for _ in range(position - 2):
        if currentNode is None:
                break
        currentNode = currentNode.next
            
    newNode.next = currentNode.next
    currentNode.next = newNode
    return head


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4

newNode = Node(4)
position = 4

traverse(node1)

addNode(node1, newNode, position)

print("added node")
traverse(node1)

