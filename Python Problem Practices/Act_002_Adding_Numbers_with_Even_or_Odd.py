
def addNumbers(a,b):
    return a + b

num1 = int(input("Input first number: ")) #input converted to integer
num2 = int(input("Input second number: "))

totalNum = addNumbers(num1, num2) # return function value assigned to a variable

if totalNum % 2 == 0: # using modulo get reminder
    print(f"{totalNum} is even") #f-string also known as string formatting
else:
    print(f"{totalNum} is odd")
