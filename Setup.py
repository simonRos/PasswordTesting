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
    file.write("reqCap: ")
    reqCaps = input("Require uppercase letter?")
    if reqCaps[0].lower() == 'y':
        file.write("True\n")
    elif reqCaps[0].lower() == 'n':
        file.write("False\n")
    else:
        file.write("\n")
    file.write("reqLow: ")
    reqLow = input("Require lowercase letter?")
    if reqLow[0].lower() == 'y':
        file.write("True\n")
    elif reqLow[0].lower() == 'n':
        file.write("False\n")
    else:
        file.write("\n")
    file.write("reqNum: ")
    reqNum = input("Require numbers?")
    if reqNum[0].lower() == 'y':
        file.write("True\n")
    elif reqNum[0].lower() == 'n':
        file.write("False\n")
    else:
        file.write("\n")
    file.write("reqSpec: ")
    reqSpec = input("Require special characters?")
    if reqSpec[0].lower() == 'y':
        file.write("True\n")
    elif reqSpec[0].lower() == 'n':
        file.write("False\n")
    else:
        file.write("\n")
    print ("Enter allowed special characters.")
    print ("Write 'Done' when you are finished: ")
    file.write("special: ")
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
