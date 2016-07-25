
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
        print "Please enter a number between 0, and 1.0"
    return strScore;

returnScore = None
while ( not(returnScore == "q")):
    returnScore = inputScore()
    print returnScore

print "Done!"


