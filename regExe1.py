import re

filelist = ("sample.txt",
            "regex_sum_302695.txt",
            "regex_sum_42.txt")

def readWholeFile(file) :
    filehandle = open(file, 'r')
    print "Processing file " + file
    # filehandle.read() reads whole file into one string, the findall find all consecutive numbers,
    # and returns them in a list of strings
    # the for loop goes through the list of strings, and convert them into float
    # [] returns the list of the float, sum works on the list of the float
    totalSum = sum ([float(x) for x in re.findall('[0-9]+',filehandle.read())])
    print totalSum
    filehandle.close()

for myfile in filelist :
    readWholeFile(myfile)
