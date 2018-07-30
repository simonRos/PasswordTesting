#Accepts information from user to determine password strength
#Simon Rosner
#5/25/2017

import os
import os.path
from StrengthTest import StrengthTest

settings = 'settings.txt'

def prompt(again=None):
    yesno = " [Yes/No] "
    ask = ""
    if again == None:
        ask = "Would you like to run the test now?" + yesno
    else:
        ask = "Would you like to run the test again?" + yesno
    response = input(ask)
    if response[0].lower() == 'y':
        operations()
    elif response[0].lower() == 'n':
        ask = "Would you like to reconfigure the test settings?" + yesno
        response = input(ask)
        if response[0].lower() == 'y':
            import Setup
            prompt()
            return
    else:
        prompt()

def operations():
    minLen = 0
    maxLen = 0
    specChar = None
    requires = {}
    #read settings file
    with open(settings,'r') as file:
        for line in file:
            spot = line.find(':') + 1
            if 'minLength: ' in line:
                minLen = line[spot:]
            elif 'maxLength: ' in line:
                maxLen = line[spot:]
            elif 'reqCap: ' in line:
                requires['reqCap'] = int(line[spot:])
            elif 'reqLow: ' in line:
                requires['reqLow'] = int(line[spot:])
            elif 'reqNum: ' in line:
                requires['reqNum'] = int(line[spot:])
            elif 'reqSpec: ' in line:
                requires['reqSpec'] = int(line[spot:])
            elif 'special: ' in line:
                specChar = line[spot:].rstrip()
            elif 'DONE' in line:
                break;        

    test = StrengthTest(minLen, maxLen, requires, specChar)
    results = test.evaluate(input("Please enter your password: "))
    os.system('cls' if os.name=='nt' else 'clear')
    outputInfo(results)
    prompt(True)
    
def outputInfo(results):
    print("Your password, "
          , results['password']
          , " is "
          , ("" if results['viable'] else "not ")
          , "valid.\nScore: "
          , results['score']
          , "\nTotal possible score: "
          , results['max']
          , "\nRating: "
          , round(results['rating'],2)
          , "%\nNotes: "
          , results['notes'])

#script
if os.path.isfile(settings):
    print("Settings found.\n")
    prompt()
else:  
    print ("No settings file has been detected.\nPerforming first time setup.\n")
    import Setup
    print ("Setup complete.\n")
    prompt()
        
