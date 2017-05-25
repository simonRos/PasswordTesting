#Accepts information from user to determine password strength
#Simon Rosner
#5/25/2017

import os
import os.path
from StrengthTest import StrengthTest

settings = 'settings.txt'

def prompt():
    response = input("Would you like to run the test now?[Yes/No] ")
    if response[0].lower() == 'y':
        operations()
    elif response[0].lower() == 'n':
        response = input("Would you like to reconfigure the test settings?[Yes/No] ")
        if response[0].lower() == 'y':
            import Setup
            return
    else:
        prompt()

def operations():
    minLen = 0
    maxLen = 0
    specChar = None
    requires = {}
    file = open(settings,'r')
    for line in file:
        spot = line.find(':') + 1
        if 'minLength: ' in line:
            minLen = line[spot:]
        elif 'maxLength: ' in line:
            maxLen = line[spot:]
        elif 'reqCap: ' in line:
            requires['reqCap'] = line[spot:]
        elif 'reqLow: ' in line:
            requires['reqLow'] = line[spot:]
        elif 'reqNum: ' in line:
            requires['reqNum'] = line[spot:]
        elif 'reqSpec: ' in line:
            requires['reqSpec'] = line[spot:]
        elif 'special: ' in line:
            specChar = line[spot:].rstrip()
        elif 'DONE' in line:
            break;        
    file.close()

    test = StrengthTest(minLen, maxLen, requires, specChar)
    results = test.evaluate(input("Please enter your password: "))
    os.system('cls' if os.name=='nt' else 'clear')
    outputInfo(results)
    
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
        
