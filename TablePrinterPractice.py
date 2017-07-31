fruits = ['apples', 'oranges', 'cherries', 'banana']
names = ['Alice', 'Bob', 'Carol', 'David']
animals = ['dogs', 'cats', 'moose', 'goose']


def printSizeOfBiggestWord(words):
    size = 0
    for word in words:
        if len(word) > size:
            size = len(word)
    print(size)


# Should print 8
print("Fruits:")
printSizeOfBiggestWord(fruits)

# Should print 5
print("Names:")
printSizeOfBiggestWord(names)

# Should also print 5
print("Animals:")
printSizeOfBiggestWord(animals)
