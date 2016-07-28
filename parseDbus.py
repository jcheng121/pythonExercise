#! /usr/bin/python

import json
def splitbyJson(line) :
    what = json.loads(line)
    return what;

def printList (list):
    for key in list:
        if type(key).__name__ == 'dict':
            printDict(key)
        else:
            print key

def printDict (audioDict) :
    for key in audioDict :
        if type(audioDict[key]).__name__ == 'list' :
            printList(audioDict[key])
        else:
            print "%20s ==> %-40s" % (key, audioDict[key])
    print "\n"

matchingArray = ["audioSources"]
messageStatistic = {}

for matching in matchingArray :
    messageStatistic[matching] = 0

lookingFor = None
keepLine = None
count = 0

dbusHandle = open ('dbus.log', 'r')

for line in dbusHandle :   
    line = line.strip()
    if lookingFor is None :
        for matching in matchingArray:
            pos = line.find(matching)
            if pos >= 0:
                lookingFor = matching
                break
    else:
        line = line.replace("string \"","")
        if not keepLine is None :
            line = keepLine + line
            line = line.replace(r'\n',"")
            line = line.rstrip("\"")
            keepLine = None
        if count == 2 :
            break;
        try:
            line = line.rstrip("\"")
            audioDict = splitbyJson(line)
        except:
            keepLine = line
            count = count + 1
            continue
        index = messageStatistic[lookingFor] = messageStatistic[lookingFor] + 1
        print "=========================================================================================="
        print "Found %d %s message!!!" % (index, lookingFor)
        print "=========================================================================================="
        printDict(audioDict)
        keepLine = None
        lookingFor = None
        count = 0
dbusHandle.close()
