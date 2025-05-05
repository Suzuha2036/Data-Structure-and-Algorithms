class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
def traverseNode(head): # print every node
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")


# we're comparing memory address
def deleteNode(head, nodeToDelete):
    
    if head ==  nodeToDelete:                                           # check if the target node is the head(first node)
        return head.next                                                # returning the next node (deleting it)
        
    currentNode = head
    #  vvv for safety check vvv | vvv for the target check vvv
    while currentNode.next and currentNode.next != nodeToDelete:        # traverse to find the node before target node
        currentNode = currentNode.next
    
    if currentNode.next is None:                                        # return head if target node isn't found
        return head
    
    currentNode.next = currentNode.next.next                            # skipping the node to be deleted
    
    
    # example of this is were deleting the 4th node so 
    # the traversing will traverse till 3rd node then it will stop
    # the currentnode.next(which is 4) = curnode.next.next (5) will work "currentNode.next = currentNode.next.next"
    # after that, making the next node for 3rd node not the 4th but the 5th
    # 1 2 3 5 skipping the 4th node
    
    return head
    
node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Before deletion:")
traverseNode(node1)

# Delete node4
node1 = deleteNode(node1, node4)

print("\nAfter deletion:")
traverseNode(node1)
    