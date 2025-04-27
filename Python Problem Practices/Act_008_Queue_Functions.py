# Queue
# Queue is like a standing line in grocery // First In First Out

# !!!!!!!!!!!!!!!!!!! ITS SAME AS STACK BUT THE POP AND QUEUE[] NEEDS TO HAVE 0 INDEX !!!!!!!!!!!!!!!!!!!!!!!!!!!
#                    queue.pop(0) and queue[0]           //          stack.pop() and stack[-1]

# Enqueue: Adds a new element to the queue                                   queue.append()
# Dequeue: Removes and returns the first (front) element from the queue      queue.pop(0)
# Peek: Returns the first element in the queue                               queue[0]
# isEmpty: Checks if the queue is empty.                                     isEmpty = not queue
# Size: Finds the number of elements in the queue.                           len(queue)

queue = [] #initialize a stack

#adding new element
queue.append('A')
queue.append('B')
queue.append('C')
queue.append('D')
print("queue: ", queue)

#peeking
firstElementAdded = queue[0]
print("First Element Added is ", firstElementAdded)

#removing the first element
queue.pop(0)        # removing A
queue.pop(0)        # removing B
print("queue: ", queue)

#size of queue
print("queue size:",len(queue))

#is empty
isEmpty = not queue             #convert the list to a boolean
print("queue is empty? ", isEmpty)



