
def calculateSalary (timeinHour, rate):
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
    canIQuit = False
    while (not canIQuit):
        try:
            what = raw_input("Enter score between 0 and 1.0 : (q to quit)")
            if what == "q" :
                print "quit from score input rootine!!!"
                canIQuit = True;
            else:
                score = float(what)
                if score > 1 or score < 0 : print "Bad score "
                elif score >= 0.9 : print "A"
                elif score >= 0.8 : print "B"
                elif score >= 0.7 : print "C"
                elif score >= 0.6 : print "D"
                else              : print "F"
        except:
            print "Please enter a number between 0, and 1.0"

max(40, 20)
