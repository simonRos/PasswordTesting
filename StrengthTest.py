#Tests viablity of a string as a password
#Simon Rosner
#5/24/2017
import string
import re
class StrengthTest:
    """Holds the rules for a password check"""
    def __init__(self, minLength, maxLength, requires, specialChars = None):
        self.requires = requires #dictionary with bool values
        self.minLength = int(minLength) #int
        self.maxLength = int(maxLength) #int
        self.length = 0
        pointHeavy = ""
        #should be an array of chars
        if specialChars == None or len(specialChars) <= 0:
            self.special = None
            pointHeavy = "Z" * self.maxLength
        else:
            self.special = ''.join(set(specialChars)) #remove dupes
            pointHeavy = specialChars[0] * self.maxLength
        #password score
        self.score = 0.0
        #is the password viable?
        self.viable = True
        #writeup
        self.notes = ""
        #calculate max
        self.max = self.__evaluate("Zz1" + pointHeavy[:-3])
    #Evaluates password length
    def __testLength(self, password):
        lengthRange = self.maxLength - self.minLength
        if self.length < self.minLength or self.maxLength < self.length:
            #autofail. No points awarded.
            self.viable = False
            self.notes += 'password does not meet the '
            if self.length > self.maxLength:
                self.notes += 'maximum'
            elif self.length < self.minLength:
                self.notes += 'minimum'
            self.notes += ' length requirement, '
            return
        elif self.length <= lengthRange/2:
            #short passwords get a score of p*length
            self.score += self.length
            self.notes += 'password could be longer, '
        elif self.length > lengthRange:
            #longer passwords get a small score boost
            self.score += 1.5*(self.length - lengthRange)
            self.score += lengthRange/2
    #more points go to more rare letters
    def __letterRarity(self, password):
        letterVal = {'z' : 1.2,
                     'q' : 0.9,
                     'x' : 0.8,
                     'j' : 0.7,
                     'k' : 0.6,'v' : 0.6,'b' : 0.6,
                     'p' : 0.5,
                     'y' : 0.4,'g' : 0.4,
                     'f' : 0.2,'w' : 0.2,'m' : 0.2,
                     'u' : 0.2,'c' : 0.2,'l' : 0.2,
                     'd' : 0.1,'r' : 0.1,'h' : 0.1,
                     's' : 0.0,'n' : 0.0,'i' : 0.0,
                     'o' : 0.0,'a' : 0.0,'t' : 0.0,
                     'e' : 0.0,}
        for char in password.lower():
            if char in letterVal:
                self.score += letterVal[char]
            
    #additional points for each capital letter
    def __capitalCount(self, password):
        tempScore = sum(1 for char in password if char.isupper())
        if tempScore < 1:
            if self.requires['reqCap']:
                self.viable = False
            self.notes += 'password must contain at least 1 uppercase letter, '
        elif tempScore == self.length:
            if self.requires['reqLow']:
                self.viable = False
            self.notes += 'password must contain at least 1 lowercase letter, '
        else:
            self.score += tempScore
    #additional points for each number character used
    def __numberCount(self, password):
        tempScore = sum(1 for char in password if char.isdigit())
        if tempScore < 1:
            if self.requires['reqNum']:
                self.viable = False
            self.notes += 'password must contain at least 1 number, '
        elif tempScore == self.length:
            if self.requires['reqNum']:
                self.viable = False
            self.notes += 'password cannot be all numbers, '
        else:
            self.score += tempScore

    #additional points for each special character used        
    def __specialCount(self, password):
        tempScore = sum(1 for char in password if (char in self.special))*2
        if tempScore < 2:       
            if self.requires['reqSpec']:
                self.viable = False
            self.notes += 'password must contain at least 1 special character, '
        elif tempScore == self.length*2:
            if self.requires['reqSpec']:
                self.viable = False
            self.notes += 'password cannot be all special characters, '
        else:
            self.score += tempScore
    def __illegalCharacter(self, password):
        pattern = "[a-zA-Z0-9"
        if self.special != None and len(self.special) > 0:
            pattern += self.special
        pattern += "]"
        for char in password:
            if re.match(pattern, char) is None:
                self.viable = False
                self.notes += 'illegal character: ' + char + ', '
    def evaluate(self, password):
        #reset fluid values
        self.score = 0.0
        self.viable = True
        self.notes = ""
        self.length = len(password)
        #run functions
        self.__testLength(password)
        self.__letterRarity(password)
        self.__capitalCount(password)
        self.__numberCount(password)
        self.__illegalCharacter(password)
        if self.special != None and len(self.special) > 0:
            self.__specialCount(password)
        #paranoid security measure
        password = None
        #return results as dictonary
        return {'password': '*' * self.length,
                'score': round(self.score,2),
                'viable': self.viable,
                'notes': self.notes[:-2],
                'max': self.max,
                'rating': self.score/(self.max/100)}
    def __evaluate(self,password):
        self.score = 0.0
        self.viable = True
        self.notes = ""
        self.length = len(password)
        #run functions
        self.__testLength(password)
        self.__letterRarity(password)
        self.__capitalCount(password)
        self.__numberCount(password)
        self.__illegalCharacter(password)
        if self.special != None and len(self.special) > 0:
            self.__specialCount(password)
        return round(self.score,2)
    
