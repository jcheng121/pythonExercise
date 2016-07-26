#! /usr/bin/python

data = " X-DSPAM-Confidence: 0.8475 "
data = data.strip()
sPos = data.find(' ')
test = data[sPos+1:]
test = test.strip()
test = float(test)
print test
print type(test)

# exercise 6.1
def traverseStrBack (data):
    index = len(data) - 1
    while index > 0 :
        print data[index]
        index = index - 1

# Exercise 6.2
fruit = "Fruit"
print type (fruit[:])

def countLetter (words, findWhat):
    count = 0
    for letter in words:
        if letter == findWhat:
            count = count + 1
    return count

print countLetter('banana', 'a')