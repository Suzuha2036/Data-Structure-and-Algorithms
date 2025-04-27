#STRINGS
word = input("Input word:")
targetCharacter = input("Input character to find: ")
index = []
length = len(word)
for iteration in range(length):
    if word[iteration] == targetCharacter:
        index.append(iteration+1)
        
print(f"Character {targetCharacter} found at index/s {index}")
