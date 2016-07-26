#! /usr/bin/python

def openFile (filename):
    try:
        fhandle = open(filename, "r")
    except:
        print "%s doesn't exist" % filename
        exit()
    return fhandle
    
def readLine (filename, lookfor, debug = False) :
    fhandle = openFile(filename)
    count = 0
    total = 0
    for line in fhandle:
        line = line.rstrip()
        pos = line.find(lookfor)
        if pos >= 0:
            count = count + 1
            line = line[pos+len(lookfor):].strip()
            total = total + float(line)
            print line
    fhandle.close()
    return count, total

def readAndUpperLine (filename):
    fhandle = openFile(filename)
    for line in fhandle:
        line = line.rstrip()
        print line.upper()
    fhandle.close()
    
def readFile (filename):
    fhandle = openFile(filename)
    entireFile = fhandle.read()
    fhandle.close()
    return len(entireFile)

filename = raw_input("Enter a file to process: ")
count, total = readLine(filename, "X-DSPAM-Confidence:",True)
print "Found %d" % count
print "Average is %.4f" % (total/count)

