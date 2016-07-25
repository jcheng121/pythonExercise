
def fibanacciRecursive (n, result):
    "This is to implement fibanacci with recursive call"
    if len(result) > n :
        return result[n]
    else:
        value = fibanacciRecursive(n-2,result) + fibanacciRecursive(n-1,result)
        result.append(value)
        return result[n]

result = [0,1,1]

def compare(n1,n2):
    if n1 > n2 : return True
    else       : return False

n = int(input("Please enter an interger: "))
fibOfN = fibanacciRecursive(n, result)
print result[n]

outputF = open("fibanacciSeq.txt", 'w')
index = 0
for value in result :
    index = index + 1
    outputF.write(str(index))
    outputF.write("\t")
    outputF.write(str(value))
    outputF.write("\n")
outputF.close()

print (compare(2,4))