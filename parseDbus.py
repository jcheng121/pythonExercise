#! /usr/bin/python
import json

def printList (list):
    for key in list:
        if type(key).__name__ == 'dict':
            printDict(key, False)
        elif type(audioDict[key]).__name__ == 'list' :
            printList(audioDict[key])
        else:
            print key

def printDict (audioDict, skipLine) :
    for key in audioDict :
        if type(audioDict[key]).__name__ == 'list' :
            printList(audioDict[key])
        elif type(audioDict[key]).__name__ == 'dict' :
            print "%s {" % key
            printDict(audioDict[key], True)
            print "}"
        else:
            print "%20s ==> %-40s" % (key, audioDict[key])
    if skipLine == False : print "\n"

# Main function starts here
lookingFor = None
keepLine   = None

matchingArray = ["selectDevice",
                 "activeDevice",
                 "operStatus",
                 "audioSources",
                 "start",
                 "deviceState"]
messageStatistic = {}

for matching in matchingArray :
    messageStatistic[matching] = 0

dbusHandle = open ('dbus.log', 'r')

for line in dbusHandle :
    line = line.strip()
    if lookingFor is None :
        for matching in matchingArray:
            lookingFor = matching
            matching = "string \"" + matching + "\""
            pos = line.find(matching)
            if pos < 0:
                lookingFor = None
                continue
            else:
                break
    else:
        line = line.replace("string \"","")
        if not keepLine is None :
            line = keepLine + line
            line = line.replace(r'\n',"")
            line = line.rstrip("\"")
            keepLine = None
        try:
            line = line.rstrip("\"")
            audioDict = json.loads(line)
        except:
            keepLine = line
            continue
        index = messageStatistic[lookingFor] = messageStatistic[lookingFor] + 1
        print "=========================================================================================="
        print "Found %d %s message!!!" % (index, lookingFor)
        print "=========================================================================================="
        printDict(audioDict, False)
        keepLine = None
        lookingFor = None
dbusHandle.close()
