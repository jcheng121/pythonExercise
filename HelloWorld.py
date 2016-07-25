
def calculateSalary (timeinHour, rate):
    "Function to calculate salary, note if you work more than 40 hours a week, your rate is bumped"
    if timeinHour > 40 : rate = rate * 1.5
    return timeinHour * rate

def inputNameSalry ():
    yourName = raw_input("Please enter your name: ")
    print "\nHello " + yourName
    yourWorkingHour = float(raw_input("Please enter hours that you worked last week : "))
    yourRate = float(raw_input("Please enter your hourly rate :" ))
    yourSalary = calculateSalary(yourWorkingHour, yourRate)
    print "\nYou have made " + str(yourSalary) +  " last week.\n"
    print "Your rate is ", yourRate

def inputScore():
    strScore = None
    try:
        what = raw_input("Enter score between 0 and 1.0 : (q to quit)")
        if what == "q" :
            strScore = what;
        else:
           score = float(what)
           if score > 1 or score < 0 : print "Bad score "
           elif score >= 0.9 : strScore ="A"
           elif score >= 0.8 : strScore ="B"
           elif score >= 0.7 : strScore ="C"
           elif score >= 0.6 : strScore ="D"
           else              : strScore ="F"
    except:
        print "Bad score"
    return strScore;

def inputData():
    data = None
    try:
        what = raw_input("Enter a number : (done or Done to quit)")
        if what == "done" or what == "Done" :
            data = "q";
        else:
            data = int(what)
    except:
        print "Invalid Input"
    return data;

returnValue = None
largest = None
while ( not(returnValue == "q" )):
    returnValue = inputData()
    if (type(returnValue) is int) and (largest is None or returnValue > largest) :
        largest = returnValue
print "Done!"
print "Largest number found: ", largest

