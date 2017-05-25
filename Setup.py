#Sets up testing parameters
#For use by test administrator
#Simon Rosner
#5/25/2017

with open('settings.txt','w+') as file:
    file.write("minLength: "
               + input("What is the minimum password length? ")
               + "\n")
    file.write("maxLength: "
               + input("What is the maximum password length? ")
               + "\n")
    file.write("special: ")
    print ("Enter allowed special characters.")
    print ("Write 'Done' when you are finished: ")
    tempChar = ''
    while tempChar != 'DONE':
        if 'DONE' in tempChar.upper():
            tempChar = tempChar.replace('DONE','')
            file.write(tempChar)
            break
        else:
            file.write(tempChar)
            tempChar = input().upper().replace(' ','') #remove whitespace
    file.write('\nDONE')
