import json

audioTable = {}
audioDictTemplate = {'displayString': None,
                     'uuid': None,
                     'id': None,
                     "isPlaying": None,
                    "isAvailable": None,
                    'audioSource': None,
                    'displayAvailable': None,
                    'appIcon': None}

def updateAudioTable (audioDict) :
    if audioDict['audioSource'] != None :
        audioTable[audioDict['audioSource']] = audioDict
    return audioTable

import json
def splitbyJson(line) :
    what = json.loads(line)
    return what;

def splitByAudioDictionary (line, audioDict):
    count = 0
    audioKeys = audioDict.keys()
    for key in audioKeys :
        posKey = line.find(key)
        if posKey >= 0 :
            tempLine     = line[posKey+len(key)+1:]
            #print tempLine;
            semiColonPos = tempLine.find(':')
            commaPos     = tempLine.find(',')
            if commaPos < 0 :
                commaPos = len(tempLine) # Reach the end of the string
            #print semiColonPos, ' ', commaPos
            audioDict[key] = tempLine[semiColonPos+1:commaPos]
            line = line[:posKey] + line[posKey + len(key) + commaPos:]
    return audioDict

dbusHandle = open ('dbus.log', 'r')
matching = "audioSources\":"

def printAudioDict (audioDict) :
    for key in audioDict :
        if not audioDict[key] is None :
            print "%20s ==> %-40s" % (key, audioDict[key])
    print "\n"

index = 0
for line in dbusHandle :
    line = line.strip()
    if not line.startswith("signal sender") and not line.startswith("method call") and not line.startswith("method return sender"):
        line = line.replace("string","")
        pos = line.find(matching)
        if pos >= 0:
            index = index + 1
            print "=========================================================================================="
            print "Found %d %s message!!!" % (index, matching[:len(matching)-3])
            print "=========================================================================================="
            pos = line.find("[")
            line = line[pos+1 : line.find("]")]
            while line != '' :
                leftBrace = line.find("{")
                rightBrace = line.find("}")
                source = line[leftBrace:rightBrace+1]
                line = line[rightBrace+1:]
                print source
                #audioDict = splitByAudioDictionary(source, audioDictTemplate)
                audioDict = splitbyJson(source)
                printAudioDict(audioDict)
dbusHandle.close()

