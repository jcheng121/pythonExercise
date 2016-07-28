#! /usr/bin/python
import json

def analyzeFrom (fmLine) :
    fromDict = {}
    lookfor = {"method call sender=:":["method call","dest"],
               "signal sender=:":["signal","dest"]}
    for lookforSender in lookfor :
        pos = fmLine.find(lookforSender)
        if pos >= 0 : 
            fmLine = fmLine[len(lookforSender):]
            content = lookfor[lookforSender]
            if not content[1] is None :
                findDestPos = fmLine.find(" -> " + content[1])
                fromSrc = fmLine[:findDestPos]
                fromSrc = fromSrc.strip()
                dest = fmLine[findDestPos+len(" -> " + content[1])+1:]
                findDestPos = dest.find("serial=")
                dest = dest[:findDestPos]
                fromDict[content[0]] = fromSrc
                fromDict[content[1]] = dest  
                fromDict["message"]  = content[0]
                return fromDict
        
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
                 "pause",
                 "stop",
                 "deviceState",
                 "playState",
                 "nowPlaying"]
messageStatistic = {}

for matching in matchingArray :
    messageStatistic[matching] = 0
    
originalFile= []
commandForm = {}
with open ('dbus.log', 'r') as dbusHandle :    
    for line in dbusHandle :
        line = line.strip()  
        originalFile.append(line) 
        if lookingFor is None :
            for matching in matchingArray:
                lookingFor = matching
                matching = "string \"" + matching + "\""
                pos = line.find(matching)
                if pos < 0:
                    lookingFor = None
                    continue
                else:
                    commandForm = analyzeFrom(originalFile[len(originalFile)-2])
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
            print "="*80
            print "Found %d %s %s !!" % (index, lookingFor, commandForm["message"])    
            print "-"*80
            printDict(commandForm, True)    
            print "-"*80    
            printDict(audioDict, False)
            keepLine = None
            lookingFor = None
dbusHandle.close()
