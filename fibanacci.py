

import random

def fibanacciRecursive (n, result):
    "This is to implement fibanacci with recursive call"
    if len(result) > n :
        return result[n]
    else:
        value = fibanacciRecursive(n-2,result) + fibanacciRecursive(n-1,result)
        result.append(value)
        return result[n]

result = [0,1,1]

def generateNumber (minNum,minMax,numbers):
    index  = 0
    result = []
    while index < numbers : 
        index = index + 1
        ranNumber = random.randint(minNum,minMax)
        result.append(ranNumber)
    return result

def print_result (result, outputF, printIndex):
    index = 0
    for value in result :
        index = index + 1
        if printIndex : 
            outputF.write(str(index))
            outputF.write("\t")
        outputF.write(str(value))
        outputF.write("\n")
        
def compare(n1,n2):
    if n1 > n2 : return True
    else       : return False

n = int(input("Please enter an interger: "))
fibOfN = fibanacciRecursive(n, result)
print result[n]

outputF = open("fibanacciSeq.txt", 'w')
print_result(result, outputF, True)
outputF.close()

result  = generateNumber(1,199, 100)
outputF = open("randomNum.txt",'w')
print_result(result,outputF, False)
outputF.close()  
