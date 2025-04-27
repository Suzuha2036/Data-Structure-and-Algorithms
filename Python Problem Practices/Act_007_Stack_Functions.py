# Stack
# Stack is like a pile of pancakes // First In Last Out

# Stack                                                             Keywords
# Push: Adds a new element on the stack.                        append
# Pop: Removes and returns the top element from the stack       pop
# Peek: Returns the top element on the stack                    topElement = stack[-1]
# isEmpty: Checks if the stack is empty                         isEmpty = not bool(stack) // or not stack
# Size: Finds the number of elements in the stack               len(stack)

stack = [] #initialize a stack

#adding new element
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack: ", stack)

#peeking
topElement = stack[-1]          # -2 and 1 gets B, -3 and 0 gets A  // top stack is -1
print("Last element is ", topElement)

#removing last element added
stack.pop()
print("Stack: ", stack)

#size of stack
print("Stack size:",len(stack))

#is empty
isEmpty = not stack             #convert the list to a boolean
print("stack is empty? ", isEmpty)



